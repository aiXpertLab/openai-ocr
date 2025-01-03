import streamlit as st
import utils.streamlit_components
utils.streamlit_components.streamlit_ui('🛸ai OCR')

import apps.llm.models

if 'ai_model' not in st.session_state:
    st.session_state.ai_model = "OpenAI"  # Initial value

ai_model2 = apps.llm.models.pick_model()

# if ai_model != st.session_state.ai_model:
#     st.session_state.ai_model = ai_model

st.info(f"You are using: {ai_model2}")
