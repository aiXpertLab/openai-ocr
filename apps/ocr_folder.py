import os, json, streamlit as st
from utils import openaiapi, pdf264

def extract_from_multiple_pages(base64_images, original_filename, output_directory):
    entire_invoice = []
    
    for index, base64_image in enumerate(base64_images, start=1):
        st.text(f"Processing page {index} of {len(base64_images)}...")
        # invoice_json = openaiapi.extract_invoice_data(base64_image)
        # if invoice_json is None:
        #     print("No JSON data extracted for page {index}.")
        # else:
        #     invoice_data = json.loads(invoice_json)
        #     entire_invoice.append(invoice_data)

        try:
            invoice_json = openaiapi.extract_invoice_data(base64_image)
            invoice_data = json.loads(invoice_json)
            entire_invoice.append(invoice_data)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError on page {index}: {e}")
            continue  # Skip to the next image


    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Construct the output file path
    output_filename = os.path.join(output_directory, original_filename.replace('.pdf', '_extracted.json'))
    
    # Save the entire_invoice list as a JSON file
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(entire_invoice, f, ensure_ascii=False, indent=4)
    return output_filename


def main_extract(read_path, write_path):
    for filename in os.listdir(read_path):
        file_path = os.path.join(read_path, filename)
        print(file_path)
        if os.path.isfile(file_path):
            base64_images = pdf264.pdf_to_base64_images(file_path)
            extract_from_multiple_pages(base64_images, filename, write_path)



if __name__ == "__main__":
    read_path= "./data/pdf"
    write_path= "./data/json"
    main_extract(read_path, write_path)