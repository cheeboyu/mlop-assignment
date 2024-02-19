from flask import Flask, request, url_for, render_template, jsonify
from pycaret.regression import *
import pickle, random
import numpy as np
import pandas as pd
from joblib import load

app = Flask(__name__)

cardio_clf = load("static\knn_model.pkl") # will change based on directory. Please copy relative path.
cardio_cols = ['Age', 'Gender', 'Weight', 'Height', 'Ap_hi', 'Ap_lo', 'Cholesterol',
       'Glucose', 'Smoke', 'Active', 'Heart_rate', 'Blood_oxygen_level',
       'Body_temp', 'Diabetic']

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/cardio', methods=['GET', 'POST'])
def cardio():
    if request.method == "POST":
        int_features = [x for x in request.form.values()]
        age = request.form.get('Age', '')
        gender = request.form.get('Gender', '')
        weight = request.form.get('Weight', '')
        height = request.form.get('Height', '')
        ap_lo = request.form.get('Ap_lo', '')
        ap_hi = request.form.get('Ap_hi', '')
        cholesterol = request.form.get('Cholesterol', '')
        glucose = request.form.get('Glucose', '')
        smoke = request.form.get('Smoke', '')
        active = request.form.get('Active', '')
        heart_rate = request.form.get('Heart_rate', '')
        blood_oxygen_level = request.form.get('Blood_oxygen_level', '')
        body_temp = request.form.get('Body_temp', '')
        diabetic = request.form.get('Diabetic', '')
        # Map gender input to integer
        int_features[1] = map_gender(int_features[1])
        data_unseen = pd.DataFrame([int_features], columns=cardio_cols)
        prediction = cardio_clf.predict(data_unseen)
        return render_template("cardio.html", prediction=prediction, submitted=True)
    else:
        return render_template("cardio.html", submitted=False)

def map_gender(gender_input):
    if gender_input.upper() == 'F':
        return 1
    elif gender_input.upper() == 'M':
        return 2
    else:
        # Handle invalid input
        return None

if __name__ == "__main__":
    app.run(debug=True)
