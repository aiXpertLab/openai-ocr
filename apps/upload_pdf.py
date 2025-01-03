import streamlit as st, os, json
from streamlit_extras.stateful_button import button

from utils import pdf264, convertGhostscript
from apps import ai_ocr

def streamlit_upload(upload_path, write_path, text_image="image"):

    uploaded_file = st.file_uploader("File uploader:", type=["pdf"])
    
    if uploaded_file is not None:
        with st.spinner('processing...'):
            # Save the uploaded file to a temporary location
            temp_file_path = os.path.join(upload_path, uploaded_file.name)
            st.warning(temp_file_path)
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_file.getbuffer())

            if text_image == "text":
                output_filename = convertGhostscript.convert_text_pdf(temp_file_path, write_path)
            else:
                base64_images   = pdf264.pdf_to_base64_images(temp_file_path)
                output_filename = ai_ocr.ai_extract(base64_images, uploaded_file.name, write_path)
        
        st.success(f"File processed successfully.")
        st.download_button(
            label="Download Extracted Data",
            data=open(output_filename, "r", encoding="utf-8").read(),
            file_name=os.path.basename(output_filename),
            mime="application/json"
        )
