import streamlit as st
from streamlit_extras.stateful_button import button

import apps.upload_pdf
import utils.streamlit_components
from config import upload_path, write_path

utils.streamlit_components.streamlit_ui('📨 Text PDF')



if button("Upload PDF to process?", key='coa41'):
    apps.upload_pdf.streamlit_upload(upload_path=upload_path, write_path=write_path, text_image="text")
