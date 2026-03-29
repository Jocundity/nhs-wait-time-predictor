# NHS Wait Time Predictor
This is a machine learning and data science project that uses real data from the UK's National Health Service (NHS) regarding Referral to Treatment (RTT) time across different providers and specialties in order to predict wait times.

## NHS Wait Time Predictor Web App
![Live Wait Time Predictor Demo](/wait_time_predictor_demo.gif)

Live Link: (https://nhs-wait-time-predictor.streamlit.app)


## Project Overview:
Delays in NHS services are a common challenge. This project predicts patient wait times using historical Referral to Treatment (RTT) data, enabling hospitals and patients to better understand expected waiting periods.

The interactive web app allows users to select a provider and specialty, and receive a predicted wait time in weeks.

## Components:
- Jupyter notebook (rtt_prediction.ipynb) for thought process, data preparation, and model creation
- Streamlit app (app.py) for the interactive web tool

## Tools Used:
- Python
- pandas and numpy for data manipulation
- matplotlib and seaborn for visualisation
- scikit-learn for machine learning and model creation
- Streamlit for web framework and web deployment

## Project Workflow:
- A raw dataset (~180,000 rows) was downloaded from the NHS website using the latest posted data (Jan 26): (https://www.england.nhs.uk/statistics/statistical-work-areas/rtt-waiting-times/rtt-data-2025-26/)
- The dataset was cleaned and transformed in SQL in order to extract relevant information for analysis. This transformed dataset is saved as rtt.csv. (See this repo for cleaning process: (https://github.com/Jocundity/Referral-to-Treatment-Waiting-Times))
- The CSV file was imported into a notebook using pandas.
- Rows with a patient count of 0 were dropped.
- Feature engineering was performed to transform columns with text-based categorical data (Provider and Specialty) into numerical data that the model can learn from using one-hot encoding.
- Linear regression model was created with sci-kit learn to predict estimated wait time in weeks based on provider and specialty.
- Patient Count column from dataset was used to weight predictions.
- Interactive web app was created with Streamlit in order to let people test the model in a user-friendly way.

  ## Model Performance Metrics:
  Mean Absolute Error (MAE) was approximately 11 weeks. This can be explained by the wide range of waiting periods in the orginal dataset (1 - 105 weeks). If extremely long waits were removed from training data, this would likely reduce the error.
