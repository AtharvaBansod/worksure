# ui/input_form.py

import streamlit as st

def render_form():
    """
    Renders the main input form for job details. The fields here directly correspond
    to the columns used in the training preprocessor.
    """
    # These options are based on the training data's categorical columns
    employment_types = ['Unknown', 'Full-time', 'Part-time', 'Contract', 'Temporary', 'Other']
    required_experience = ['Unknown', 'Internship', 'Not Applicable', 'Mid-Senior level', 'Associate', 'Entry level', 'Executive', 'Director']
    required_education = ['Unknown', "Bachelor's Degree", "Master's Degree", "High School or equivalent", "Unspecified", "Some College Coursework Completed", "Vocational", "Certification", "Associate Degree", "Professional", "Doctorate", "Some High School Coursework"]

    st.header("📝 Enter Job Details")
    st.markdown("Provide as much detail as possible for the most accurate prediction.")
    
    st.subheader("Core Textual Information")
    job_title = st.text_input("Job Title *", help="Enter the exact title of the job posting.")
    description = st.text_area("Job Description *", height=250, help="Paste the entire body of the job description here. This is a critical field.")
    requirements = st.text_area("Requirements", height=150, help="List specific skills or qualifications required.")
    
    st.subheader("Company & Benefits")
    col1, col2 = st.columns(2)
    with col1:
        company_profile = st.text_area("Company Profile", height=150, help="A brief overview of the company.")
    with col2:
        benefits = st.text_area("Benefits", height=150, help="Detail the benefits or perks provided.")

    st.subheader("Categorical Information")
    c1, c2, c3 = st.columns(3)
    with c1:
        employment_type = st.selectbox("Employment Type", options=employment_types)
    with c2:
        required_experience_level = st.selectbox("Required Experience", options=required_experience)
    with c3:
        required_education_level = st.selectbox("Required Education", options=required_education)

    # This dictionary structure exactly matches the columns your preprocessor was trained on.
    # 'description_word_count' is calculated later in utils.py.
    # 'industry' and 'function' are defaulted to 'Unknown' to match the fillna() in your notebook.
    input_data = {
        "title": job_title,
        "company_profile": company_profile,
        "description": description,
        "requirements": requirements,
        "benefits": benefits,
        "employment_type": employment_type,
        "required_experience": required_experience_level,
        "required_education": required_education_level,
        "industry": 'Unknown',
        "function": 'Unknown',
    }
    return input_data