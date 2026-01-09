import streamlit as st
import requests

st.title("Bengaluru House Price Prediction")

# Inputs
total_sqft = st.number_input("Total Square Feet Area", min_value=0.0)
bath = st.number_input("Number of Bathrooms", min_value=0)
balcony = st.number_input("Number of Balconies", min_value=0)

area_type = st.selectbox("Area Type", ['Super built-up  Area', 'Built-up  Area', 'Plot  Area', 'Carpet  Area'])
availability = st.selectbox("Availability", ['Ready To Move', 'Immediate Possession', '18-Dec-21', '19-Dec-21'])  # shortened for clarity
size = st.selectbox("Size", ['2 BHK', '3 BHK', '4 BHK'])  # shortened
society = st.selectbox("Society", ['Coomee', 'Theanmp', 'Soiewre'])  # shortened
location_input = st.text_input('Enter Location')

# Prediction block
if st.button("Predict Price"):
    user_input = {
        "total_sqft": total_sqft,
        "bath": bath,
        "balcony": balcony,
        "area_type": area_type,
        "availability": availability,
        "location": location_input,
        "size": size,
        "society": society
    }

    try:
        response = requests.post('http://localhost:5000/predict', json=user_input)
        if response.status_code == 200:
            predicted_price = response.json().get('predicted_price')
            st.success(f"The predicted price of the house is: ₹ {predicted_price} Lakhs")
        else:
            st.error("Prediction failed. Server returned an error.")
    except Exception as e:
        st.error(f"Request failed: {e}")