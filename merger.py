import os
from PyPDF2 import PdfWriter

merger = PdfWriter()
path = '/Users/hrsheldon/PycharmProjects/PDFMerger/docsToMerge'  # absolute path to directory with files
files = os.listdir(path)

# Loop through files in the specified directory
for filename in files:
    if filename.endswith(".pdf"):
        print(f"Appending: {filename}")
        file_path = os.path.join(path, filename)  # Get full file path
        merger.append(file_path)  # append file to end

# Write the combined PDF file after appending all PDFs
with open("combinedDocs.pdf", "wb") as output_pdf:
    merger.write(output_pdf)

# Close the PdfWriter object after writing the file
merger.close()
