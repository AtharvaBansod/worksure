# app.py

import streamlit as st
from utils import load_artifacts, predict
from ui.input_form import render_form
from ui.results_display import display_results # Assuming you have this file from the previous answer

# --- Page Configuration ---
st.set_page_config(
    page_title="Fake Job Posting Detector",
    page_icon="🕵️‍♂️",
    layout="wide",
)

# --- Load Artifacts ---
preprocessor, models = load_artifacts()

# --- App Header ---
st.title("🕵️‍♂️ Fake Job Posting Detector")
st.markdown("""
This tool uses a suite of machine learning models to analyze job postings and predict their authenticity. 
Fill out the form below to get an instant analysis.
""")
st.write("---")

# --- Main Application Logic ---
if models is None or preprocessor is None:
    st.stop()
else:
    # Render the input form
    input_data = render_form()
    
    st.write("---")
    
    # The primary action button
    if st.button("Analyze Job Posting", type="primary", use_container_width=True):
        if not input_data['title'] or not input_data['description']:
            st.warning("Please fill in at least the 'Job Title' and 'Job Description' fields.")
        else:
            with st.spinner("Analyzing... Models are at work! 🤖"):
                # Perform prediction
                results = predict(input_data, preprocessor, models)
                
                # Display the results
                display_results(results)