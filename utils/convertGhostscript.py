import subprocess, platform, os

def convert_text_pdf(local_input_filename, output_directory):
    # Detect the operating system
    if platform.system() == "Windows":
        gs_command = "gswin64c"  # Use the Windows executable for Ghostscript
    else:
        gs_command = "gs"  # Use the Linux path for Ghostscript

    os.makedirs(output_directory, exist_ok=True)

    # Construct the output file path
    local_output_filename = os.path.join(output_directory, os.path.basename(local_input_filename).replace('.pdf', '_text.txt'))


    subprocess.call([gs_command,
                     "-q",
                     "-dNOPAUSE",
                     "-dBATCH",
                     "-sDEVICE=txtwrite",
                     f"-sOutputFile={local_output_filename}",
                     f"{local_input_filename}"])
    return local_output_filename

# convert_pdf_to_text('example.pdf', 'textgs.txt')
