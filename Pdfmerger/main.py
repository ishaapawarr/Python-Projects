import PyPDF2
import os

pdffiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    with open(filename, 'rb') as pdfFile:
        merger.append(pdfFile)

output_path = 'merged.pdf'
with open(output_path, 'wb') as output_file:
    merger.write(output_file)

merger.close()
os.startfile(output_path)
