# utils.py

import pandas as pd
import joblib
import streamlit as st

@st.cache_resource
def load_artifacts():
    """
    Loads the preprocessor and all trained models from disk.
    Caches the result to avoid reloading on every user interaction.
    """
    try:
        preprocessor = joblib.load('models/preprocessor.pkl')
        models = {
            "Logistic Regression": joblib.load('models/logistic_model.pkl'),
            "Random Forest": joblib.load('models/random_forest_model.pkl'),
            "Naive Bayes": joblib.load('models/naive_bayes_model.pkl')
        }
        return preprocessor, models
    except FileNotFoundError:
        st.error("Model or preprocessor files not found. Please ensure the 'models' directory and its contents are correct.")
        return None, None

def predict(input_data, _preprocessor, _models):
    """
    Takes user input, creates the required features, preprocesses it, and returns predictions.
    """
    # Create a DataFrame from the input dictionary
    input_df = pd.DataFrame([input_data])
    
    # --- THIS IS THE FIX ---
    # Create the 'description_word_count' feature just like in the training script
    input_df['description_word_count'] = input_df['description'].apply(lambda x: len(x.split()))
    
    # Now, the DataFrame has all the columns the preprocessor expects.
    # Preprocess the input data
    processed_input = _preprocessor.transform(input_df)
    
    # Generate predictions and probabilities
    results = {}
    for name, model in _models.items():
        prediction = model.predict(processed_input)[0]
        probability = model.predict_proba(processed_input)[0]
        prob_of_prediction = probability[prediction]
        results[name] = {"prediction": prediction, "probability": prob_of_prediction}
        
    return results