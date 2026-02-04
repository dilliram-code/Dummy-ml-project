# app.py

import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.title("🏠 House Price Prediction App")

st.write("Enter house size to predict price")

# User input
size = st.number_input("House Size (sqft)", min_value=100, max_value=5000, step=50)

# Prediction
if st.button("Predict Price"):
    size_array = np.array([[size]])
    prediction = model.predict(size_array)
    st.success(f"Estimated Price: {prediction[0]:.2f} lakhs")
