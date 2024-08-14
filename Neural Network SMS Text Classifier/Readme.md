# SMS Spam Classification Using Machine Learning

This project involves classifying SMS messages as either "ham" (normal messages) or "spam" (advertisements or unsolicited messages). The project is completed in Python using the SMS Spam Collection dataset.

## Project Overview

The notebook was originally developed in Google Colaboratory, and I have saved the final version as a Python file locally. The project includes the following steps:

1. **Data Import and Preprocessing:**
   - Imported the necessary libraries and the SMS Spam Collection dataset.
   - Preprocessed the text data to make it suitable for model training.

2. **Model Building and Training:**
   - Developed a machine learning model to classify SMS messages as "ham" or "spam".
   - Trained the model using the provided training dataset.
   - Created a function `predict_message` that takes a message string as input and returns a list with:
     - A probability score between 0 and 1 indicating the likelihood of the message being "ham" (0) or "spam" (1).
     - The predicted label "ham" or "spam".

3. **Model Evaluation:**
   - Evaluated the model using the testing dataset to ensure its accuracy and generalization capabilities.

4. **Function Testing:**
   - The final cell in the notebook tests the `predict_message` function and checks the model's performance on unseen data.

## Getting Started

To run the project, clone this repository and run the Python file locally. The project requires Python and the necessary libraries such as Pandas, Scikit-learn, and NLTK.

```bash
git clone https://github.com/yourusername/sms-spam-classification.git
cd sms-spam-classification
python sms_spam_classification.py
