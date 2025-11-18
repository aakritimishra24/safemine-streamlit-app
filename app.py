import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

st.title("⛏️ SafeMine Rockfall Risk Predictor")

# -------------------------
# Load your trained model
# -------------------------
try:
    # Load only the model (do not unpack)
    model = joblib.load("rockfall_risk_model.pkl")  # ensure this file is in your repo
except FileNotFoundError:
    st.error("Model file 'rockfall_risk_model.pkl' not found. Upload it to your GitHub repo.")
    st.stop()

# -------------------------
# Input fields for app users
# -------------------------
ore_grade = st.number_input("Ore Grade (%)", min_value=0.0, max_value=10.0, value=2.5)
tonnage = st.number_input("Tonnage", min_value=0.0, value=1000.0)
ore_value = st.number_input("Ore Value (¥/tonne)", min_value=0.0, value=4000.0)
mining_cost = st.number_input("Mining Cost (¥)", min_value=0.0, value=1200.0)
processing_cost = st.number_input("Processing Cost (¥)", min_value=0.0, value=800.0)
profit = st.number_input("Profit (¥)", min_value=0.0, value=2500000.0)

# -------------------------
# Prediction
# -------------------------
if st.button("Predict Risk"):
    input_df = pd.DataFrame([{
        "Ore_Grade (%)": ore_grade,
        "Tonnage": tonnage,
        "Ore_Value (¥/tonne)": ore_value,
        "Mining_Cost (¥)": mining_cost,
        "Processing_Cost (¥)": processing_cost,
        "Profit (¥)": profit
    }])

    try:
        prediction = model.predict(input_df)[0]
        st.success(f"Predicted Rockfall Risk: {prediction}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
        st.stop()

    # -------------------------
    # Graph: Rockfall Risk vs Ore Grade
    # -------------------------
    st.subheader("📊 Rockfall Risk Trend with Ore Grade")

    ore_range = np.linspace(0, 10, 25)

    graph_df = pd.DataFrame([{
        "Ore_Grade (%)": og,
        "Tonnage": tonnage,
        "Ore_Value (¥/tonne)": ore_value,
        "Mining_Cost (¥)": mining_cost,
        "Processing_Cost (¥)": processing_cost,
        "Profit (¥)": profit
    } for og in ore_range])

    try:
        risk_values = model.predict(graph_df)
    except Exception as e:
        st.error(f"Error generating graph: {e}")
        st.stop()

    # Plot
    fig, ax = plt.subplots()
    ax.plot(ore_range, risk_values, marker="o", linestyle="-", color="orange")
    ax.set_xlabel("Ore Grade (%)")
    ax.set_ylabel("Predicted Risk Level")
    ax.set_title("Ore Grade vs Rockfall Risk")
    ax.grid(True)

    st.pyplot(fig)
    st.markdown(f"### 📊 Predicted Rockfall Risk: **{risk_level}**")

THRESHOLD = 0.5

if risk_level >= THRESHOLD:
    st.error("🚨 ALERT: HIGH ROCKFALL RISK DETECTED!")
else:
    st.success("🟢 SAFE: Rockfall risk is low.")
