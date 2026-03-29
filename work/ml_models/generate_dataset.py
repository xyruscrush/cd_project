import pandas as pd
import random

def generate_sample():

    loc = random.randint(5,300)
    is_unused = random.choice([0,1])
    contains_sensitive = random.choice([0,1])
    num_params = random.randint(0,6)
    cyclomatic_complexity = random.randint(1,20)
    commit_count = random.randint(0,60)
    code_churn = random.randint(0,1500)
    days_since_last_edit = random.randint(0,1200)
    author_count = random.randint(1,12)

    recent_modification = 1 if days_since_last_edit < 30 else 0


 
    if is_unused == 1:
        usage_score = 0
    elif commit_count < 5:
        usage_score = 1
    elif commit_count < 20:
        usage_score = 2
    else:
        usage_score = 3


    if days_since_last_edit > 365:
        activity_score = 0
    elif days_since_last_edit > 90:
        activity_score = 1
    elif days_since_last_edit > 30:
        activity_score = 2
    else:
        activity_score = 3



    importance = 0

    if loc > 100:
        importance += 1

    if cyclomatic_complexity > 10:
        importance += 1

    if author_count > 5:
        importance += 1

    if num_params > 3:
        importance += 1

    importance_score = min(importance,3)

    if contains_sensitive == 0:
        sensitivity_score = 0
    else:
        sensitivity_score = 2

        if loc > 50:
            sensitivity_score = 3


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
        usage_score,
        activity_score,
        importance_score,
        sensitivity_score
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
    "usage_score",
    "activity_score",
    "importance_score",
    "sensitivity_score"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("code_analysis_dataset.csv", index=False)

print("Dataset generated!")