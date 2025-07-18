

import streamlit as st

def display_results(results):
    """
    Displays the prediction results from all models in a structured, visual way.
    """
    st.write("---")
    st.subheader("📊 Prediction Results")
    
    # --- Create a summary card at the top ---
    overall_fake_votes = sum(1 for res in results.values() if res['prediction'] == 1)
    num_models = len(results)
    
    st.markdown("#### Consensus Verdict")
    if overall_fake_votes > num_models / 2: # Majority fraudulent
         st.error(f"⚠️ **Overall Consensus: FRAUDULENT** ({overall_fake_votes}/{num_models} models agree)")
         st.warning("This job posting shows strong signals associated with fraudulent listings. Please exercise extreme caution.")
    else:
        st.success(f"✅ **Overall Consensus: LEGITIMATE** ({num_models - overall_fake_votes}/{num_models} models agree)")
        st.info("While the models suggest this post is real, always perform due diligence before applying or sharing personal information.")

    st.markdown("---")
    st.markdown("#### Individual Model Predictions")
    
    # Create columns for each model's detailed result
    cols = st.columns(num_models)
    
    for i, (model_name, result) in enumerate(results.items()):
        with cols[i]:
            prediction = result['prediction']
            probability = result['probability']
            
            st.markdown(f"**{model_name}**")
            
            if prediction == 1:
                st.markdown(f"<p style='color:red;'>Prediction: FAKE</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='color:green;'>Prediction: REAL</p>", unsafe_allow_html=True)

            st.write("Confidence:")
            st.progress(probability)
            st.markdown(f"<p style='text-align: right; margin-top: -10px; font-size: 0.9em;'>{probability:.2%}</p>", unsafe_allow_html=True)