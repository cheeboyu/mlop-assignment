# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("boyu_api")

# Create input/output pydantic models
input_model = create_model("boyu_api_input", **{'accommodates': 2, 'bathrooms': 1.0, 'bed_type': 'Real Bed', 'bedrooms': 1.0, 'beds': 1.0, 'cancellation_policy': 'moderate', 'guests_included': 2, 'has_availability': 't', 'host_is_superhost': 'f', 'host_listings_count': 1.0, 'instant_bookable': 'f', 'property_type': 'House', 'review_scores_rating': nan, 'room_type': 'Private room'})
output_model = create_model("boyu_api_output", prediction=89.0)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
