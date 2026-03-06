import ast
import os

SENSITIVE_KEYWORDS = ["password", "passwd", "secret", "api_key", "token"]

class StaticAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.functions = {}
        self.function_calls = set()
        self.variables = {}
        self.used_variables = set()
        self.sensitive_entities = set()

    def visit_FunctionDef(self, node):
        self.functions[node.name] = {
            "lineno": node.lineno,
            "is_unused": True,
            "contains_sensitive": False
        }
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.function_calls.add(node.func.id)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id
                self.variables[var_name] = {
                    "lineno": node.lineno,
                    "is_unused": True,
                    "contains_sensitive": False
                }

                for keyword in SENSITIVE_KEYWORDS:
                    if keyword in var_name.lower():
                        self.sensitive_entities.add(var_name)

        self.generic_visit(node)

    def visit_Name(self, node):
        self.used_variables.add(node.id)
        self.generic_visit(node)

    def finalize(self):
        for func in self.function_calls:
            if func in self.functions:
                self.functions[func]["is_unused"] = False

        for var in self.used_variables:
            if var in self.variables:
                self.variables[var]["is_unused"] = False

        for var in self.sensitive_entities:
            if var in self.variables:
                self.variables[var]["contains_sensitive"] = True

        return self.functions, self.variables


def analyze_file(filepath):
    with open(filepath, "r") as f:
        code = f.read()

    tree = ast.parse(code)
    analyzer = StaticAnalyzer()
    analyzer.visit(tree)

    return analyzer.finalize()


if __name__ == "__main__":
    functions, variables = analyze_file("sample.py")

    print("Functions:")
    print(functions)

    print("\nVariables:")
    print(variables)