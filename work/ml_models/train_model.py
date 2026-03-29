import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

df = pd.read_csv("code_analysis_dataset.csv")

X = df[[
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
]]

y = df[[
    "usage_score",
    "activity_score",
    "importance_score",
    "sensitivity_score"
]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

base_model = RandomForestClassifier(n_estimators=200)

model = MultiOutputClassifier(base_model)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Model accuracy:", accuracy)

joblib.dump(model, "code_analysis_model.pkl")

print("Model saved!")