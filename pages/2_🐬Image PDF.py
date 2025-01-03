import streamlit as st
from streamlit_extras.stateful_button import button

import apps.upload_pdf, apps.llm.models
import utils.streamlit_components
from config import upload_path, write_path


utils.streamlit_components.streamlit_ui('🦣 Image PDF')


if button("Upload image-PDF?", key='a411'):
    apps.upload_pdf.streamlit_upload(
        upload_path = upload_path, 
        write_path  = write_path, 
        text_image  = "image"
    )
