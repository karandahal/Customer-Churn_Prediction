# Customer Churn Prediction

This project focuses on predicting customer churn for a business, using machine learning techniques to identify customers who are likely to leave the service. The goal is to help businesses retain valuable customers by predicting churn early, so appropriate retention strategies can be implemented.

## Table of Contents

- [Overview](#overview)
- [Data](#data)
- [Technologies Used](#technologies-used)
- [Model Building](#model-building)
- [Streamlit Web App](#streamlit-web-app)


## Overview

Customer churn refers to the loss of customers over time. This project aims to build a machine learning model that can predict whether a customer is likely to churn based on various features, such as demographic data, account details, service usage patterns, and customer feedback.

## Data

The dataset used in this project contains information about customers, including:

- **Customer ID**: Unique identifier for each customer.
- **Demographic information**: Age, gender, location, etc.
- **Account information**: Subscription plan, contract type, account tenure.
- **Service usage**: Frequency of service usage, complaints, support interactions.
- **Churn**: Binary label indicating if the customer churned (1) or stayed (0).

The dataset is publicly available from [Data Source Link] (if applicable).

## Technologies Used

- **Python**: Programming language used for analysis and modeling.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computing.
- **Scikit-learn**: Machine learning models and tools.
- **Matplotlib**: Data visualization.
- **Jupyter Notebooks**: For data exploration and visualization.


## Model Building

The churn prediction model is built using the following steps:

1. **Data Preprocessing**: Cleaning the dataset by handling missing values, encoding categorical features, and scaling numerical features.
2. **Feature Selection**: Identifying the most relevant features for churn prediction.
3. **Model Training**: Training various machine learning models (e.g., Logistic Regression, Random Forest, XGBoost) to predict customer churn.
4. **Model Evaluation**: Using metrics such as Accuracy, Precision, Recall, and F1-score to evaluate the performance of the model.

## Streamlit Web App

In addition to running the model through Jupyter or the command line, this project also includes a **Streamlit web app** for a more interactive user experience.

### To run the web app:

1. Ensure you have installed the required dependencies, including Streamlit:
   ```bash
   pip install streamlit
   ```
2. Start the app by running
   ``` bash
   streamlit run app.py
    ```
3.  Once the app is running, you will see a user-friendly interface where you can input various customer attributes (e.g., age, gender, service usage, etc.) and click the "Predict" button to see if the customer is likely to churn.

5. The predictions will be displayed directly on the web page, along with relevant details such as the likelihood of churn, which will help businesses make data-driven decisions.


