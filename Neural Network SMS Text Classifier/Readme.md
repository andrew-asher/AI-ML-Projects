# Healthcare Cost Prediction Using Regression

This project involves predicting healthcare costs using a regression algorithm. The project is completed in Python using a dataset that contains various features related to individuals, including their healthcare costs. The goal is to build a model that can accurately predict healthcare expenses based on new data.

## Project Overview

The notebook was originally developed in Google Colaboratory, and I have saved the final version as a Python file locally. The project includes the following steps:

1. **Data Import and Preprocessing:**
   - Imported the necessary libraries and the dataset.
   - Handled categorical data by converting them into numerical values.
   - Split the dataset into training (80%) and testing (20%) sets.
   - Created labels for training and testing by popping off the `expenses` column.

2. **Model Building and Training:**
   - Developed a regression model to predict healthcare costs.
   - Trained the model using the training dataset.
   - Evaluated the model using the testing dataset to ensure it generalizes well.

3. **Model Evaluation:**
   - The model was evaluated using the Mean Absolute Error (MAE) metric.
   - The target was to achieve an MAE of under 3500, meaning the model predicts healthcare costs with an error of less than $3500.

4. **Results Visualization:**
   - Plotted the predicted versus actual healthcare costs using the test dataset.

## Getting Started

To run the project, clone this repository and run the Python file locally. The project requires Python and the necessary libraries such as Pandas, NumPy, Matplotlib, and TensorFlow/Keras.

```bash
git clone https://github.com/yourusername/healthcare-cost-prediction.git
cd healthcare-cost-prediction
python healthcare_cost_prediction.py
