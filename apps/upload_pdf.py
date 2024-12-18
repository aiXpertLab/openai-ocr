import streamlit as st, os, json
from utils import openaiapi, pdf264
from apps import ocr_folder

def streamlit_upload_and_process(upload_path, write_path):
    
    # Streamlit file uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        with st.spinner('processing...'):
            # Save the uploaded file to a temporary location
            temp_file_path = os.path.join(upload_path, uploaded_file.name)
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_file.getbuffer())
            
            # Process the uploaded file
            base64_images = pdf264.pdf_to_base64_images(temp_file_path)
            output_filename = ocr_folder.extract_from_multiple_pages(base64_images, uploaded_file.name, write_path)
            
        st.success(f"File processed successfully. Extracted data saved at: {output_filename}")
        st.download_button(
            label="Download Extracted Data",
            data=open(output_filename, "r", encoding="utf-8").read(),
            file_name=os.path.basename(output_filename),
            mime="application/json"
        )
