import streamlit as st
import pandas as pd

# Load data function
@st.cache
def load_data():
    # data = pd.read_excel("gwkerela2023.xlsx", header=5)
    predictions = pd.read_csv("output1.csv")
    return predictions

# Function to filter data based on user input
def get_predictions(lat, lon, district, predictions):
    filtered_data = predictions[
        (predictions['Latitude'] == lat) &
        (predictions['Longitude'] == lon) &
        (predictions['District Name'] == district)
    ]
    return filtered_data

# Streamlit UI
st.title("Mineral and Element Prediction")

# User Inputs
st.sidebar.header("Input Parameters")
latitude = st.sidebar.text_input("Latitude")
longitude = st.sidebar.text_input("Longitude")
district_name = st.sidebar.text_input("District Name")

# Load data
predictions = load_data()

# Get predictions
if latitude and longitude and district_name:
    try:
        prediction_table = get_predictions(float(latitude), float(longitude), district_name, predictions)
        st.write("### Prediction Table")
        st.write(prediction_table)
    except ValueError:
        st.write("Please enter valid numeric values for latitude and longitude.")
else:
    st.write("Please enter latitude, longitude, and district name to get predictions.")

