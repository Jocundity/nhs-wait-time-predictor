import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Load features
with open("feature_columns.pkl", "rb") as file:
    feature_columns = pickle.load(file)

# Load provider names
with open("providers.pkl", "rb") as file:
    providers = pickle.load(file)

# Load specialty names
with open("specialties.pkl", "rb") as file:
    specialties = pickle.load(file)


st.title("NHS Wait Time Predictor")
st.write("Select a provider and specialty to estimate your wait time.")


# Dropdowns for provider and specialty
provider_input = st.selectbox("Choose a provider: ", providers)
specialty_input = st.selectbox("Choose a specialty: ", specialties)

# Wait time prediction function
def predict_wait_time(provider, specialty):
    # Create a dataframe with one row and fill it withe zeros
    row = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

    # Set correct columns to 1 for the correct provider and specialty
    provider_column = "provider_" + provider
    specialty_column = "specialty_" + specialty
    
    if provider_column in row.columns:
        row[provider_column] = 1
   
    if specialty_column in row.columns:
        row[specialty_column] = 1
 
    #  Use model to predict wait time
    prediction = model.predict(row)[0]
    return round(prediction, 2)

# Predict button
if st.button("Predict Wait Time", icon=":material/calendar_clock:", type="primary"):
    result = predict_wait_time(provider_input, specialty_input)
    st.success(f"Predicted Wait Time: {result} weeks")

  