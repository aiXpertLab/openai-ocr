import streamlit as st, os, json
<<<<<<< HEAD
from streamlit_extras.stateful_button import button

from utils import pdf264, convertGhostscript
from apps import ai_ocr

def streamlit_upload(upload_path, write_path, text_image="image"):

    uploaded_file = st.file_uploader("File uploader:", type=["pdf"])
=======
from utils import openaiapi, pdf264, convertGhostscript
from apps import ocr_folder

def streamlit_upload_and_process(upload_path, write_path, text_image="image"):
    
    # Streamlit file uploader
    if text_image == "text":
        uploaded_file = st.file_uploader("Upload a Text PDF", type=["pdf"])
    else:
        uploaded_file = st.file_uploader("Upload a Image PDF file", type=["pdf"])
>>>>>>> 53790b2447945238b9cc3782701a72115fc5b2ed
    
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
<<<<<<< HEAD
                base64_images   = pdf264.pdf_to_base64_images(temp_file_path)
                output_filename = ai_ocr.ai_extract(base64_images, uploaded_file.name, write_path)
        
        st.success(f"File processed successfully.")
=======
                base64_images = pdf264.pdf_to_base64_images(temp_file_path)
                output_filename = ocr_folder.extract_from_multiple_pages(base64_images, uploaded_file.name, write_path)
        
        st.success(f"File processed successfully. Extracted data saved at: {output_filename}")
>>>>>>> 53790b2447945238b9cc3782701a72115fc5b2ed
        st.download_button(
            label="Download Extracted Data",
            data=open(output_filename, "r", encoding="utf-8").read(),
            file_name=os.path.basename(output_filename),
            mime="application/json"
        )
