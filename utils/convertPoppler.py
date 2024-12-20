import subprocess

def convert_pdf_to_text(local_input_filename, local_output_filename):
    try:
        # Run the pdftotext command
        subprocess.run(['pdftotext', local_input_filename, local_output_filename], check=True)
        print(f"Successfully converted {local_input_filename} to {local_output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# Example usage
convert_pdf_to_text('example.pdf', 'text.txt')