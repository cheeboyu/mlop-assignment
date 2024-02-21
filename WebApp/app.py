# Importing necessary libraries
from flask import Flask, request, render_template
from pycaret.regression import *
import pandas as pd
from joblib import load

# Creating a Flask web application instance
app = Flask(__name__)

# Load the trained machine learning model
rental_model = load("models/boyu_model.pkl")

# Define the columns for input features
rental_cols = ['bathrooms', 'bedrooms', 'accommodates', 'beds', 'review_scores_rating']

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

# Run the Flask web application
if __name__ == "__main__":
    app.run(debug=True)