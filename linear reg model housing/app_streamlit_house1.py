import numpy as np 
import pandas as pd
import pickle 
import streamlit as st

# Load the model correctly
with open(r"C:\Users\ajcho\OneDrive\Desktop\full stack data science and AI\BY SELF\ML\ML self\Linear_housing_model.pkl", "rb") as pickle_in:
    classifier = pickle.load(pickle_in)

# Fix function syntax and return value
def predict_housing(MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude):
    prediction = classifier.predict([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    return prediction

# Define main function
def main():
    st.title('House Price Prediction')

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Price Prediction App</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields
    MedInc = st.text_input('Enter the Median Income', '')
    HouseAge = st.text_input('Enter the House Age', '')
    AveRooms = st.text_input('Enter the Average Number of Rooms', '')
    AveBedrms = st.text_input('Enter the Average Number of Bedrooms', '')
    Population = st.text_input('Enter the Population', '')
    AveOccup = st.text_input('Enter the Average Occupancy', '')
    Latitude = st.text_input('Enter the Latitude', '')
    Longitude = st.text_input('Enter the Longitude', '')

    result = ''
    
    if st.button('Predict'):
        try:
            # Convert inputs to float before passing to the model
            MedInc = float(MedInc)
            HouseAge = float(HouseAge)
            AveRooms = float(AveRooms)
            AveBedrms = float(AveBedrms)
            Population = float(Population)
            AveOccup = float(AveOccup)
            Latitude = float(Latitude)
            Longitude = float(Longitude)

            # Get prediction
            result = predict_housing(MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude)
            st.success(f'The predicted house price is ${result[0]:,.2f}')
        except ValueError:
            st.error('Please enter valid numbers.')

    if st.button('About'):
        st.text("Let's Learn!")
        st.text('This app predicts house prices based on input features.')

# Run the app correctly
if __name__ == '__main__':
    main()
