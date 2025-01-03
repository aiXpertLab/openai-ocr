import os, json, streamlit as st
from apps.llm import ai_api

def ai_extract(base64_images, original_filename, output_directory ):
    
    entire_invoice = []
    
    for index, base64_image in enumerate(base64_images, start=1):
        st.text(f"Processing page {index} of {len(base64_images)}...")

        try:
            invoice_json = ai_api.extract_from_b64(base64_image=base64_image, page_number=index)
            invoice_data = json.loads(invoice_json)
            entire_invoice.append(invoice_data)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError on page {index}: {e}")
            continue  # Skip to the next image
        except Exception as e:
            print(f"An unexpected error occurred on page {index}: {e}")
            continue  # Skip to the next image

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Construct the output file path
    output_filename = os.path.join(output_directory, original_filename.replace('.pdf', '_extracted.json'))
    
    # Save the entire_invoice list as a JSON file
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(entire_invoice, f, ensure_ascii=False, indent=4)
    return output_filename

