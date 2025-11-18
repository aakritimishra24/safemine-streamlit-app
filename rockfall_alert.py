import streamlit as st
import pandas as pd

# Assuming prediction data is in a CSV on GitHub, or enter manually
st.title("🪨 Rockfall Risk Prediction Alert")

# Load existing data from a CSV file (Optional)
uploaded_file = st.file_uploader("Upload Prediction CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Prediction Data:")
    st.dataframe(df)

    # Assuming your CSV has a column named 'prediction'
    if 'prediction' in df.columns:
        threshold = st.slider("Set Rockfall Risk Threshold", 0.0, 0.5)
        df['alert'] = df['prediction'] >= threshold
        st.write("Alert Status:")
        st.dataframe(df[['prediction', 'alert']])

        # Visual alert
        if df['alert'].any():
            st.error("🚨 WARNING: Rockfall Risk Detected!")
            st.write("👁️‍🗨️ Check your buzzer, LED, or vibrator for alert.")
        else:
            st.success("✔️ No Rockfall Risk Detected")
else:
    st.info("Please upload a CSV with prediction data.")

# Manual Input Testing
st.header("Manual Test")
prediction_value = st.number_input("Enter a rockfall prediction value (0-1):", 0.0, 0.0, 0.0)
threshold_manual = 0.5

if prediction_value >= threshold_manual:
    st.error("🚨 ALERT: Rockfall risk high!")
else:
    st.success("✔️ Safe")
