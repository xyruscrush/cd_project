import pandas as pd
import random

def generate_sample():

    loc = random.randint(5, 300)
    is_unused = random.choice([0,1])
    contains_sensitive = random.choice([0,1])
    num_params = random.randint(0,6)
    cyclomatic_complexity = random.randint(1,20)
    commit_count = random.randint(0,60)
    code_churn = random.randint(0,1500)
    days_since_last_edit = random.randint(0,1200)
    author_count = random.randint(1,12)

    recent_modification = 1 if days_since_last_edit < 30 else 0

    if is_unused == 0 and recent_modification == 1:
        state = 0   

    elif is_unused == 0 and recent_modification == 0:
        state = 1   

    elif is_unused == 1 and recent_modification == 1:
        state = 2 

    else:
        state = 3   

    if contains_sensitive == 1:
        label = state + 4
    else:
        label = state

    return [
        loc,
        is_unused,
        contains_sensitive,
        num_params,
        cyclomatic_complexity,
        commit_count,
        code_churn,
        days_since_last_edit,
        author_count,
        recent_modification,
        label
    ]


data = [generate_sample() for _ in range(5000)]

columns = [
    "loc",
    "is_unused",
    "contains_sensitive",
    "num_params",
    "cyclomatic_complexity",
    "commit_count",
    "code_churn",
    "days_since_last_edit",
    "author_count",
    "recent_modification",
    "label"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("dead_code_dataset.csv", index=False)

print("Dataset generated successfully!")