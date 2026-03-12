import joblib
import numpy as np

model = joblib.load("dead_code_model.pkl")

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


sample1 = np.array([[80,0,0,2,4,20,300,10,3,1]])

sample2 = np.array([[25,1,0,1,2,2,20,400,1,0]])

sample3 = np.array([[50,1,1,3,6,1,10,800,1,0]])

samples = [sample1, sample2, sample3]

for i, sample in enumerate(samples, start=1):

    prediction = model.predict(sample)[0]

    print(f"Sample {i} Prediction:", labels[prediction])