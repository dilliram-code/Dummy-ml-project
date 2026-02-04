# 🏠 House Price Prediction using Machine Learning & Streamlit

This is a beginner-friendly machine learning project that demonstrates how a trained ML model can be deployed as a web application using **Streamlit**.  
The app takes a house size (in square feet) as input and predicts the estimated house price.

The main goal of this project is to learn the complete workflow of:
- training a machine learning model  
- saving the trained model  
- building a simple user interface  
- deploying the application online  

---

## 📌 Project Overview

- **Model**: Linear Regression  
- **Input**: House size (sqft)  
- **Output**: Estimated house price  
- **UI Framework**: Streamlit  
- **Deployment**: Render / Streamlit Cloud  

This project is intentionally kept simple so that beginners can clearly understand how machine learning deployment works in practice.

---

## 📁 Project Structure

```
ml_streamlit_app/
│
├── app.py # Streamlit application
├── train_model.py # Model training script
├── model.pkl # Saved trained model
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

---

## 🧠 How the Project Works

1. A simple dataset is created to represent house size and price.
2. A Linear Regression model is trained using scikit-learn.
3. The trained model is saved as a `.pkl` file.
4. Streamlit loads the saved model and provides a web interface.
5. Users enter house size and get a predicted price instantly.

---
