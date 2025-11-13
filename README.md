# EV Price Prediction Project – Week 3

This project focuses on predicting the price of Electric Vehicles (EVs) using Machine Learning. 
The original dataset did not include price values, so I generated a realistic synthetic price column 
(price_inr) and trained a regression model to estimate EV prices based on various features.

---

## What This Project Does

1. Loads an EV dataset containing battery, range, brand, model, etc.
2. Generates a realistic synthetic price column using:
   - brand segment (budget, mid-range, premium, luxury)
   - battery capacity
   - driving range
   - body type (SUV, sedan, hatchback)
   - small random noise
3. Applies ML preprocessing:
   - handling numeric + categorical columns
   - scaling numeric features
   - one-hot encoding categorical features
4. Trains 3 regression models:
   - Linear Regression
   - Random Forest
   - XGBoost
5. Selects the best model (Linear Regression)
6. Saves it as: ev_price_model.pkl
7. Builds a Streamlit web app that predicts EV prices based on user inputs.
8. Deploys the web app on Streamlit Cloud.

---

## Week 3 Improvements

- Added a synthetic price column with a realistic formula.
- Cleaned and standardized all dataset columns.
- Improved price model to reduce noise and increase accuracy.
- Achieved around **0.78 R²** using Linear Regression (best model).
- Updated the chatbot to predict EV price instead of range.
- Built a Streamlit UI to collect user inputs and show predicted price.
- Deployed the model and UI online using Streamlit Cloud.

---

## Files Included

- ev_chatbot_streamlit.py  → Streamlit web UI
- ev_price_model.pkl       → Trained ML model
- electric_vehicles_spec_2025.csv (updated with price_inr)
- requirements.txt         → Libraries needed for deployment
- README (this file)

---

## How to Run Locally

1. Install required libraries:
   pip install -r requirements.txt

2. Run the Streamlit app:
   streamlit run ev_chatbot_streamlit.py

---

## Deployment

The project is deployed using Streamlit Cloud.
You can open the app from this link:

https://week3evproject-88fgyq7ws8tmez3tvio4hs.streamlit.app/

---

## Summary

This project demonstrates:
- dataset preparation
- synthetic feature engineering
- regression model building
- model evaluation
- Streamlit UI development
- cloud deployment

It completes all Week 3 requirements including ML training, improvement, and UI creation.
