import streamlit as st
import pandas as pd
from pickle import load

# Function to create the page layout
def create_page():
    st.title('Gold Price Prediction for year 2022')
    st.image('gold_image.jpeg', use_column_width=True)  # Added image of gold
    
    # Dropdown for selecting month
    month = st.selectbox('Choose prediction month', range(1, 13))
    
    # Converted selected month to DataFrame
    pred_date = pd.DataFrame({'year': [2022], 'month': [month], 'day': [1]})
    features_timestamp = pd.to_datetime(pred_date)
    
    return features_timestamp

# Load the model
with open('pred.pkl', 'rb') as f:
    loaded_model = load(f)

# Get features and make prediction
features = create_page()
if st.button('Submit'):
    res = loaded_model.predict(start=features[0], end=features[0])
    st.write(f"Price of gold for the entered month is {round(res[0],2)}")
