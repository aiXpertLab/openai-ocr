import streamlit as st

from streamlit_extras.stateful_button import button
import apps.ocr_folder
import apps.upload_pdf
from utils import (streamlit_components, )
import apps

streamlit_components.streamlit_ui('🐬🦣 OCR 🍃🦭')
# -----------------------------------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Upload text-PDF", "Upload image-PDF", "OCR Email", "OCR Cloud", "OCR1"])

read_path   = "./data/pdf"
write_path  = "./data/json"
upload_path = "./data/upload"

with tab1:
    if button("Upload text-PDF to process?", key='coa41'):
        apps.upload_pdf.streamlit_upload_and_process(upload_path=upload_path, write_path=write_path, text_image="text")


with tab2:
    if button("Upload PDF to process?", key='coa42'):
        apps.upload_pdf.streamlit_upload_and_process(upload_path=upload_path, write_path=write_path, text_image="image")


with tab3:
    if button("OCR from email folder?", key='coa43'):
        apps.ocr_folder.main_extract(read_path, write_path)

