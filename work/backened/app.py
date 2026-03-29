from flask import Flask, request, jsonify
from flask_cors import CORS
import os, shutil, ast, joblib
import git

app = Flask(__name__)
CORS(app)

# -------- MODEL LOADER --------
def find_model():
    BASE_SEARCH = "/home/xyrus/Cd"

    for root, dirs, files in os.walk(BASE_SEARCH):
        if "code_analysis_model.pkl" in files:
            return os.path.join(root, "code_analysis_model.pkl")

    return None

MODEL_PATH = find_model()

if MODEL_PATH is None:
    raise Exception("❌ Model file not found!")

print("✅ Model loaded from:", MODEL_PATH)

model = joblib.load(MODEL_PATH)

# -------- CLEAN GITHUB URL --------
def clean_github_url(url):
    try:
        if "github.com" not in url:
            return None

        parts = url.strip().split("/")
        if len(parts) < 5:
            return None

        user = parts[3]
        repo = parts[4]

        clean_url = f"https://github.com/{user}/{repo}"
        return clean_url

    except:
        return None

# -------- FEATURE EXTRACTION --------
def extract_features(code):
    loc = len(code.splitlines())
    num_params = 0
    complexity = 1

    try:
        tree = ast.parse(code)
    except:
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            num_params += len(node.args.args)
        elif isinstance(node, (ast.If, ast.For, ast.While)):
            complexity += 1

    return [
        loc,
        0,
        int("password" in code.lower()),
        num_params,
        complexity,
        5,
        loc * 2,
        100,
        1,
        0
    ]

# -------- CLONE REPO --------
def clone_repo(url):
    repo_path = os.path.join(os.getcwd(), "repo")

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    print("📦 Cloning:", url)

    try:
        git.Repo.clone_from(url, repo_path, depth=1)
    except Exception as e:
        raise Exception(f"Git clone failed: {str(e)}")

    return repo_path

# -------- ANALYZE --------
def analyze_repo(repo_path):
    results = []

    print("🔍 Scanning files...")

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                try:
                    with open(path, "r", errors="ignore") as f:
                        code = f.read()

                    features = extract_features(code)
                    if features is None:
                        continue

                    pred = model.predict([features])[0]

                    results.append({
                        "file": file,
                        "usage": int(pred[0]),
                        "activity": int(pred[1]),
                        "importance": int(pred[2]),
                        "sensitivity": int(pred[3])
                    })

                except Exception as e:
                    print("⚠️ Error in file:", file, e)

    print("✅ Total files analyzed:", len(results))

    if len(results) == 0:
        raise Exception("No Python files found in repo")

    return results

# -------- API --------
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        print("\n📥 Request received")

        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"error": "No URL provided"}), 400

        clean_url = clean_github_url(url)

        if not clean_url:
            return jsonify({"error": "Invalid GitHub URL"}), 400

        print("🔗 Clean URL:", clean_url)

        repo_path = clone_repo(clean_url)

        result = analyze_repo(repo_path)

        print("🎉 Analysis completed")

        return jsonify(result)

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)