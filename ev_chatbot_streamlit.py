# ev_chatbot_streamlit.py
import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="EV Price Prediction Chatbot", page_icon="💰", layout="centered")

st.title("💰 EV Price Prediction Chatbot")
st.write("Welcome! Enter your EV specifications below to estimate its expected price in INR.")

# --- Load Model ---
@st.cache_resource
def load_model():
    return joblib.load("linear_regression_model.pkl")

# --- Load Dataset for reference ---
@st.cache_data
def load_data():
    df = pd.read_csv("electric_vehicles_spec_2025.csv")
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("/", "_").str.lower()
    
    # Features: everything except price and source_url
    X_sample = df.drop(columns=["price_inr", "source_url"], errors="ignore")
    return X_sample

model = load_model()
X_sample = load_data()

# --- User Input Form ---
st.subheader("🔧 Input EV Specifications")

user_input = {}
for col in X_sample.columns:
    if X_sample[col].dtype != "object":
        user_input[col] = st.number_input(
            f"{col}", value=float(X_sample[col].median())
        )
    else:
        user_input[col] = st.text_input(
            f"{col}", value=str(X_sample[col].mode()[0])
        )

# --- Predict Button ---
if st.button("🔮 Predict EV Price"):
    try:
        user_df = pd.DataFrame([user_input])
        pred = model.predict(user_df)[0]

        # Format price with commas
        price_str = f"{pred:,.0f}"

        st.success(f"💰 **Estimated EV Price:** ₹{price_str}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# --- Footer ---
st.caption("Developed for Week 3 Submission – EV AI Chatbot Project (Price Prediction Version)")
