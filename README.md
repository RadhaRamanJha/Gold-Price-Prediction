# Gold-Price-Prediction
# Gold Price Prediction

🔍 Business Objective  
The objective of this project is to forecast future gold prices using historical price data and time series forecasting techniques to support investment and market decision-making.

📂 Project Overview  

1. Data Collection  
Historical gold price data was collected through self-extraction and ExcelR-provided sources.  
The consolidated dataset was stored in `Gold_data_Excel.csv` for further analysis.

2. Data Cleaning & Preprocessing  
Handled missing values and inconsistent entries.  
Converted date formats and ensured time-series continuity.  
Feature engineering performed for forecasting readiness.

3. Exploratory Data Analysis (EDA)  
Trend, seasonality, and variability of gold prices were analyzed.  
Line plots and rolling statistics were used to visualize long-term trends.  
Stationarity and pattern behavior were examined.

4. Model Building  
Time series forecasting models applied:  
- Double Exponential Smoothing (DES)  
- Triple Exponential Smoothing (TES)  

The trained model was saved using Pickle as `pred.pkl`.

5. Model Evaluation  
Forecast accuracy evaluated using error metrics and visual comparison between actual and predicted prices.  
Model stability and trend-following capability were verified.

🚀 Deployment  
The trained model was deployed using a Python application (`run.py`) to allow users to predict future gold prices interactively.

📁 Files Included  
- Gold_data_Excel.csv – Dataset used for training  
- gold_price_prediction_EDA.ipynb – Exploratory Data Analysis  
- model_building_gold_price.ipynb – Model training notebook  
- pred.pkl – Saved forecasting model  
- run.py – Deployment script  
- gold_image.jpeg – Project image  
- README.md – Project documentation  

🔗 Author  
Radha Raman Jha  
GitHub Repository: https://github.com/RadhaRamanJha/Gold-Price-Prediction

