#female ->1 , male -> 0
# churn yes ->1 , else 0
#scaler file is saved as scaler.pkl
# order of the X is 'Age', 'Gender', 'Tenure', 'MonthlyCharges'

import streamlit as  st 
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")



st.title("Customer Churn Prediction App")

st.divider()

st.write("Please enter the value and press the predoct button for prediction.")

st.divider()

age = st.number_input("Enter age", min_value = 10 , max_value = 100)

tenure = st.number_input("Enter tenure", min_value = 0, max_value = 130, value =10)

monthly_charge = st.number_input("Enter monthly charge", min_value = 30, max_value =150)

gender = st.selectbox("Enter the gender",["Male","Female"])


st.divider()

predictbutton = st.button("Predict!")

st.divider()

if predictbutton:

    gender_selected = 1 if gender == "Female" else 0

    X = [age, gender_selected, tenure,monthly_charge]

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    predicted = "Churn" if prediction == 1 else "Not Churn"

    st.balloons()

    st.write(f"Prediction : {predicted}")

else:
    st.write("Please enter the value and use the predict button")
