# telco_churn
Machine Learning Assignment 01

## Project Overview
This project was my first assignment in the introductory Machine Learning class for the Business Analytics Master at Nova SBE. The project aims to predict customer churn for a telecommunications company using machine learning techniques, and the famous dataset from Kaggle contains both demographic and contract data. 

## Objectives
- Perform exploratory data analysis (EDA) to understand the dataset.
- Preprocess the data to handle missing values, encode categorical variables, and scale numerical features.
- Train and evaluate multiple machine learning models to predict customer churn.
- Select the best model based on performance metrics and interpret the results.

## Files
- `63529_Churn_Notebook.ipynb`: Contains the complete notebook (EDA, Pre-processing, modelling, pipelining)
- `63529_Pipeline`: Contains the model pipeline in a .pkl format (only Random Forest)
- `feature_engineering.py`: Contains the feature_engineering used in pipeline
- `2767ML_assignment1_data.csv`: Training data
- `2767ML_assignment1_externalvalidation_data_toStudents.xls`: Testing data for pipeline (just format; real test data is hidden to students)

## Requirements
- `63529_requirements.txt`

## Usage
1. Clone the repository.
2. Install the required packages (command: "%pip install -r 63529_requirements.txt").
3. Run the main notebook OR the pipeline itself

## Conclusion
The Random Forest model was the optimal choice with a high accuracy and precision in predicting customer churn. It outperformed other models in terms of performance metrics, making it a reliable model for this task.