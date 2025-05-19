import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/dementia_model.pkl")

st.title("🧠 Dementia Risk Predictor")
st.write("Enter patient data to assess the risk of dementia.")

# User inputs
age = st.slider("Age", 60, 100, 75)
educ = st.slider("Years of Education", 0, 25, 12)
mmse = st.slider("MMSE Score (0–30)", 0, 30, 25)
etiv = st.number_input("Estimated Total Intracranial Volume (eTIV)", 1000, 2500, 1500)
nwbv = st.number_input("Normalized Whole Brain Volume (nWBV)", 0.60, 0.90, 0.75)
ses = st.selectbox("Socioeconomic Status (1 = highest, 5 = lowest)", [1, 2, 3, 4, 5])

# When the button is clicked...
if st.button("Predict Dementia Risk"):
    # Arrange features in the same order used during training
    input_data = np.array([[age, educ, mmse, etiv, nwbv, ses]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ This patient is at risk of dementia.")
    else:
        st.success("✅ This patient is likely not demented.")



