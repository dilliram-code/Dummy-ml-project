# train_model.py

import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Simple dataset
X = np.array([500, 800, 1000, 1200, 1500]).reshape(-1, 1)
y = np.array([50, 80, 100, 120, 150])  # price in lakhs

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
