from flask import Flask, request, render_template
from pycaret.regression import *
import pandas as pd
from joblib import load

app = Flask(__name__)

diabetes_clf = load("HuiXin\diabetes_rf.pkl")
diabetes_cols = ['BloodPressure', 'BloodOxygenLevel', 'BodyTemperature', 'Glucose', 'Insulin', 'BMI', 'Age']

cardio_clf = load("Lavanya\knn_model.pkl")
cardio_cols = ['Age', 'Gender', 'Weight', 'Height', 'Ap_hi', 'Ap_lo', 'Cholesterol',
       'Glucose', 'Smoke', 'Active', 'Heart_rate', 'Blood_oxygen_level',
       'Body_temp', 'Diabetic']

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/mushroom', methods=['GET', 'POST'])
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
        return render_template("mushroom.html", prediction=prediction, submitted=True)
    else:
        return render_template("mushroom.html", submitted=False)
# Cardio gender mapping
def map_gender(gender_input):
    if gender_input.upper() == 'F':
        return 1
    elif gender_input.upper() == 'M':
        return 2
    else:
        # Handle invalid input
        return None

@app.route('/rental', methods=['GET', 'POST'])
def diabetes():
    if request.method == "POST":
        int_features = [x for x in request.form.values()]
        # print(int_features)
        BloodPressure = request.form.get('BloodPressure', '')
        BloodOxygenLevel = request.form.get('BloodOxygen', '')
        BodyTemperature = request.form.get('BodyTemp', '')
        Glucose = request.form.get('Glucose', '')
        Insulin = request.form.get('Insulin', '')
        BMI = request.form.get('BMI', '')
        Age = request.form.get('Age', '')
            
        data_unseen = pd.DataFrame([int_features], columns=diabetes_cols)
        # print(data_unseen)
        prediction = diabetes_clf.predict(data_unseen)
        return render_template("rental.html", prediction=prediction, submitted=True)

    else:
        return render_template("rental.html", submitted=False)

if __name__ == "__main__":
    app.run(debug=True)