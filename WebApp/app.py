# Importing necessary libraries
from flask import Flask, request, render_template
from pycaret.regression import *
import pandas as pd
from joblib import load

# Creating a Flask web application instance
app = Flask(__name__)

# Load the trained machine learning model
rental_model = load("models/boyu_model.pkl")
mushroom_model = load("models/final_mushroom_model2.pkl")

# Define the columns for input features
rental_cols = ['bathrooms', 'bedrooms', 'accommodates', 'beds', 'review_scores_rating']
mushroom_cols = ['odor', 'spore-print-color', 'gill-color', 'ring-type',
                 'gill-size', 'bruises', 'gill-spacing', 'cap-shape', 'cap-color', 'cap-surface']

# Define route for the home page
@app.route("/")
def home():
    return render_template("home.html")

# Define route for the rental prediction page
@app.route('/rental', methods=['GET', 'POST'])
def predict_rental():
    if request.method == "POST":
        # Get input values from the form
        bathrooms = request.form.get('bathrooms', '')
        bedrooms = request.form.get('bedrooms', '')
        accommodates = request.form.get('accommodates', '')
        beds = request.form.get('beds', '')
        review_scores_rating = request.form.get('review_scores_rating', '')

        # Validate input fields
        if not (bathrooms and bedrooms and accommodates and beds and review_scores_rating):
            return render_template("rental.html", error_message="Please fill in all the fields.")

        try:
            # Convert input values to float
            bathrooms = float(bathrooms)
            bedrooms = float(bedrooms)
            accommodates = float(accommodates)
            beds = float(beds)
            review_scores_rating = float(review_scores_rating)
        except ValueError:
            return render_template("rental.html", error_message="Invalid input. Please enter numerical values.")

        # Create DataFrame with input values
        data_unseen = pd.DataFrame(
            [[bathrooms, bedrooms, accommodates, beds, review_scores_rating]],
            columns=rental_cols)

        # Add default values for missing columns
        missing_columns = ['guests_included', 'host_listings_count', 'bed_type', 'cancellation_policy',
                           'has_availability', 'host_is_superhost', 'instant_bookable',
                           'property_type', 'room_type']
        for col in missing_columns:
            # Assigning default value of 1 for missing columns
            data_unseen[col] = 1

        # Perform prediction
        prediction = rental_model.predict(data_unseen)

        # Round the prediction to 2 decimal places
        prediction_rounded = round(prediction[0], 2)

        # Render template with prediction result
        return render_template("rental.html", prediction=prediction_rounded, submitted=True)

    else:
        return render_template("rental.html", submitted=False)


@app.route('/mushroom', methods=['GET', 'POST'])
def predict_mushroom():
    if request.method == "POST":
        # Get input values from the form
        odor = request.form.get('odor', '')
        sporecolor = request.form.get('sporecolor', '')
        gillcolor = request.form.get('gillcolor', '')
        ringtype = request.form.get('ringtype', '')
        gillsize = request.form.get('gillsize', '')
        bruises = request.form.get('bruises', '')
        gillspacing = request.form.get('gillspacing', '')
        capshape = request.form.get('capshape', '')
        capcolor = request.form.get('capcolor', '')
        capsurface = request.form.get('capsurface', '')

        # Validate input fields
        # fields_to_validate2 = ['odor','spore-print-color','gill-color','ring-type','gill-size', 'bruises', 'gill-spacing', 'cap-shape','cap-color','cap-surface']

        # Validate input fields
        if not all([odor, sporecolor, gillcolor, ringtype, gillsize, bruises, gillspacing, capshape, capcolor, capsurface]):
            return render_template("mushroom.html", error_message="Please fill in all the fields.")

        # Create DataFrame with input values
        data_unseen2 = pd.DataFrame({
            'odor': [odor],
            'spore-print-color': [sporecolor],
            'gill-color': [gillcolor],
            'ring-type': [ringtype],
            'gill-size': [gillsize],
            'bruises': [bruises],
            'gill-spacing': [gillspacing],
            'cap-shape': [capshape],
            'cap-color': [capcolor],
            'cap-surface': [capsurface]
        })

        # Perform prediction
        prediction2 = mushroom_model.predict(data_unseen2)
        predictionlabel = prediction2[0]
        print("Prediction:", predictionlabel)  # for debugging

        # Render template with prediction result
        return render_template("mushroom.html", predictionlabel=predictionlabel, odor=odor, bruises=bruises, submitted=True)

    else:
        return render_template("mushroom.html", submitted=False)

# Run the Flask web application
if __name__ == "__main__":
    app.run(debug=True)