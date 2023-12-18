import os
import PyPDF2
import sys

merger = PyPDF2.PdfFileMerger()

for filename in os.listdir(os.curdir):
    if filename.endswith(".pdf"):
        print(filename)
        merger.append(filename)
    merger.write("combinedDocs.pdf")