import os
from PyPDF2 import PdfWriter

merger = PdfWriter()

for filename in os.listdir(os.curdir):
    if filename.endswith(".pdf"):
        print(filename)
        merger.append(filename)
    merger.write("combinedDocs.pdf")

merger.close()
