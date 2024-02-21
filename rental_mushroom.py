import streamlit as st
import pandas as pd
from pycaret.regression import *
from joblib import load

# Load the trained machine learning model
rental_model = load("models/boyu_model.pkl")

# Define the columns for input features
rental_cols = ['bathrooms', 'bedrooms',
               'accommodates', 'beds', 'review_scores_rating']

# Define function for rental price prediction


def predict_rental_price(bathrooms, bedrooms, accommodates, beds, review_scores_rating):
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
    return round(prediction[0], 2)

# Define the Streamlit app


def main():
    # CSS styles
    st.markdown(
        """
        <style>
        /* CSS styles */
        body {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # HTML content
    st.markdown(
        """
        <div class="container">
            <h1>Welcome to our Machine Learning Model Prediction and Classification!</h1>
            <p>Our platform allows you to predict the rental price of budget accommodation provided by Homely Hotels and Homes.</p>
            <h2>To get started, please enter the details of the accommodation below:</h2>
            <form id="rentalForm">
                <label for="bathrooms">Number of Bathrooms (1 - 8):</label><br>
                <input type="number" id="bathrooms" name="bathrooms" min="1" max="8"><br>
                <label for="bedrooms">Number of Bedrooms (1 - 10):</label><br>
                <input type="number" id="bedrooms" name="bedrooms" min="1" max="10"><br>
                <label for="accommodates">Accommodates (1 - 16):</label><br>
                <input type="number" id="accommodates" name="accommodates" min="1" max="16"><br>
                <label for="beds">Number of Beds (1 - 16):</label><br>
                <input type="number" id="beds" name="beds" min="1" max="16"><br>
                <label for="review_scores_rating">Review Scores Rating (20 - 100):</label><br>
                <input type="number" id="review_scores_rating" name="review_scores_rating" min="20" max="100"><br><br>
                <input type="button" value="Predict Rental Price" onclick="predict()">
            </form>
            <h2 id="predictionResult"></h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # JavaScript code
    st.markdown(
        """
        <script>
        // JavaScript code
        function predict() {
            var bathrooms = parseFloat(document.getElementById("bathrooms").value);
            var bedrooms = parseFloat(document.getElementById("bedrooms").value);
            var accommodates = parseFloat(document.getElementById("accommodates").value);
            var beds = parseFloat(document.getElementById("beds").value);
            var review_scores_rating = parseFloat(document.getElementById("review_scores_rating").value);

            // Make prediction request to Streamlit app
            var predictionRequest = {
                "bathrooms": bathrooms,
                "bedrooms": bedrooms,
                "accommodates": accommodates,
                "beds": beds,
                "review_scores_rating": review_scores_rating
            };

            // Call Streamlit function to get prediction
            Streamlit.sendMessage(JSON.stringify(predictionRequest));
        }

        // Listen for prediction result from Streamlit
        Streamlit.setComponentValueListener(function(message) {
            document.getElementById("predictionResult").innerText = "Predicted Rental Price: $" + message;
        });
        </script>
        """,
        unsafe_allow_html=True
    )


# Run the Streamlit app
if __name__ == "__main__":
    main()