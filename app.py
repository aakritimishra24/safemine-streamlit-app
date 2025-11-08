import streamlit as st
import pandas as pd
import joblib

# Title
st.title("⛏️ SafeMine: AI-Based Rockfall Risk Predictor")

# Load your trained model
model = joblib.load("rockfall_risk_model.pkl")

# Input section
st.header("Enter Mining Block Details")

ore_grade = st.number_input("Ore Grade (%)", min_value=0.0, max_value=10.0, value=2.5)
tonnage = st.number_input("Tonnage", min_value=0.0, value=1000.0)
ore_value = st.number_input("Ore Value (¥/tonne)", min_value=0.0, value=4000.0)
mining_cost = st.number_input("Mining Cost (¥)", min_value=0.0, value=1200.0)
processing_cost = st.number_input("Processing Cost (¥)", min_value=0.0, value=800.0)
profit = st.number_input("Profit (¥)", min_value=0.0, value=2500000.0)

# Prediction
if st.button("Predict Risk Level"):
    df = pd.DataFrame([{
        "Ore_Grade (%)": ore_grade,
        "Tonnage": tonnage,
        "Ore_Value (¥/tonne)": ore_value,
        "Mining_Cost (¥)": mining_cost,
        "Processing_Cost (¥)": processing_cost,
        "Profit (¥)": profit
    }])
    
    prediction = model.predict(df)[0]
    st.success(f"Predicted Rockfall Risk Level: {prediction}")
