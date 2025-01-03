import streamlit as st
import utils.streamlit_components
utils.streamlit_components.streamlit_ui('🛸ai OCR')

import apps.llm.models

<<<<<<< HEAD
if 'ai_model' not in st.session_state:
    st.session_state.ai_model = "OpenAI"  # Initial value
=======
streamlit_components.streamlit_ui('🐬🦣 OCR 🍃🦭')
# -----------------------------------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Upload text-PDF", "Upload image-PDF", "OCR Email", "OCR Cloud", "OCR1"])
>>>>>>> 53790b2447945238b9cc3782701a72115fc5b2ed

ai_model2 = apps.llm.models.pick_model()

<<<<<<< HEAD
# if ai_model != st.session_state.ai_model:
#     st.session_state.ai_model = ai_model
=======
with tab1:
    if button("Upload text-PDF to process?", key='coa41'):
        apps.upload_pdf.streamlit_upload_and_process(upload_path=upload_path, write_path=write_path, text_image="text")


with tab2:
    if button("Upload PDF to process?", key='coa42'):
        apps.upload_pdf.streamlit_upload_and_process(upload_path=upload_path, write_path=write_path, text_image="image")


with tab3:
    if button("OCR from email folder?", key='coa43'):
        apps.ocr_folder.main_extract(read_path, write_path)
>>>>>>> 53790b2447945238b9cc3782701a72115fc5b2ed

st.info(f"You are using: {ai_model2}")
