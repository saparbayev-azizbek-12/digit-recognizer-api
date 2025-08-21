import joblib
import numpy as np

model = joblib.load("app/models/digit_clf.joblib")

def predict(array: np.array):
    return model.predict(array)