from flask import Flask, jsonify, render_template, request
from joblib import load
import os

app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def predict():
    clt = load("algo_classification.joblib")
    array_tweet = [request.args.get("tweet")]
    print("TYPE :  {}".format(type(array_tweet)))
    predict_value = clt.predict(array_tweet)
    print("PREDICT : {}".format(predict_value))
    return render_template("form_add_tweet.htm", value=predict_value[0])
    
@app.route("/")
def add_tweet():
    return render_template("form_add_tweet.htm")
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000))) 