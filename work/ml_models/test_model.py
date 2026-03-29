import joblib
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

model = joblib.load("code_analysis_model.pkl")

columns = [
    "loc","is_unused","contains_sensitive","num_params",
    "cyclomatic_complexity","commit_count","code_churn",
    "days_since_last_edit","author_count","recent_modification"
]

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

    return [
        loc,is_unused,contains_sensitive,num_params,
        cyclomatic_complexity,commit_count,code_churn,
        days_since_last_edit,author_count,recent_modification
    ]


samples = [generate_sample() for _ in range(300)]

df = pd.DataFrame(samples, columns=columns)

predictions = model.predict(df)

pred_df = pd.DataFrame(
    predictions,
    columns=[
        "usage",
        "activity",
        "importance",
        "sensitivity"
    ]
)

labels = ["usage","activity","importance","sensitivity"]

with PdfPages("code_analysis_report.pdf") as pdf:

    for label in labels:

        plt.figure()

        pred_df[label].value_counts().sort_index().plot(kind="bar")

        plt.title(label.upper()+" SCORE DISTRIBUTION")

        plt.xlabel("Degree (0-3)")

        plt.ylabel("Number of Functions")

        pdf.savefig()

        plt.close()

print("Report generated: code_analysis_report.pdf")