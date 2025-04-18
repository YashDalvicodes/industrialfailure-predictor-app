import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("failure_predictor_model.pkl")

st.title("🛠️ Industrial Failure Prediction App")

st.write("Enter the machine parameters below to predict if failure is likely.")

# 1. Product Type (L = Low, M = Medium, H = High)
product_type = st.selectbox("Type of Product", ["L", "M", "H"])

# Encode product type as numerical (as used in model)
product_mapping = {"L": 0, "M": 1, "H": 2}
product_encoded = product_mapping[product_type]

# 2. Air temperature
air_temp = st.number_input("Air Temperature (°C)", format="%.2f")

# 3. Process temperature
process_temp = st.number_input("Process Temperature (°C)", format="%.2f")

# 4. Rotational speed
rot_speed = st.number_input("Rotational Speed (rpm)", format="%.2f")

# 5. Torque
torque = st.number_input("Torque (Nm)", format="%.2f")

# 6. Tool wear
tool_wear = st.number_input("Tool Wear (min)", format="%.2f")

# Combine all features in correct order
input_data = np.array([[product_encoded, air_temp, process_temp, rot_speed, torque, tool_wear]])

# Predict
if st.button("Predict Failure"):
    prediction = model.predict(input_data)
    result = "⚠️ Failure Likely" if prediction[0] == 1 else "✅ No Failure Expected"
    st.success(result)