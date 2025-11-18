import requests
import time

# URL to your raw JSON file on GitHub
PREDICTION_URL = "https://raw.githubusercontent.com/<your-username>/<safemine-streamlit-app>/main/prediction.json"

# Threshold for Rockfall Prediction alert
THRESHOLD = 0.75

def get_prediction():
    response = requests.get(PREDICTION_URL)
    if response.status_code == 200:
        data = response.json()
        return data.get("prediction", 0)
    else:
        print("Error fetching prediction. Status code:", response.status_code)
        return None

def alert_system():
    prediction = get_prediction()
    if prediction is not None:
        print(f"Current Prediction: {prediction}")
        if prediction > THRESHOLD:
            print("🚨 ALERT! Risk of Rockfall detected!")
            # TODO: add hardware code here later (vibrator/LED control)
        else:
            print("Rockfall Risk is low/normal.")

if __name__ == "__main__":
    while True:
        alert_system()
        time.sleep(5)  # Check every 5 seconds

