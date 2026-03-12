import joblib
import pandas as pd
import random
import matplotlib.pyplot as plt

model = joblib.load("dead_code_model.pkl")

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
    "recent_modification"
]

labels = {
    0: "ACTIVE_FREQUENT_CHANGE",
    1: "ACTIVE_STABLE",
    2: "DEVELOPMENT_PHASE",
    3: "DEAD_CODE",
    4: "ACTIVE_FREQUENT_CHANGE + SENSITIVE",
    5: "ACTIVE_STABLE + SENSITIVE",
    6: "DEVELOPMENT_PHASE + SENSITIVE",
    7: "DEAD_CODE + SENSITIVE"
}


def generate_valid_sample():

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
        recent_modification
    ]



num_samples = 50

data = [generate_valid_sample() for _ in range(num_samples)]

df = pd.DataFrame(data, columns=columns)


predictions = model.predict(df)

df["prediction"] = predictions
df["prediction_label"] = df["prediction"].map(labels)

print("\nSample Predictions:\n")
print(df.head(10))


label_counts = df["prediction_label"].value_counts()

plt.figure()

label_counts.plot(kind="bar")

plt.title("Dead Code Prediction Distribution")

plt.xlabel("Prediction Type")

plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()