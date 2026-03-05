import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

st.title("Credit Card Fraud Detection")

amount = st.number_input("Enter Transaction Amount")

if st.button("Predict"):

    data = np.array([[amount]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Fraud Transaction 🚨")
    else:
        st.success("Normal Transaction ✅")
