from typing import Optional
from joblib import load
from fastapi import FastAPI

app = FastAPI()


@app.get("/predict/{tweet}")
def predict(tweet : str):
    clf = load("algo_classification.joblib")
    data = str([tweet])
    predict_value = clf.predict_proba([data])[0]
    return {"Hate speech": predict_value[0], "Offensive language" : predict_value[1], "Neither" : predict_value[2]}
