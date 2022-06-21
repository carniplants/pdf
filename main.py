from PyPDF2 import PdfReader, PdfFileWriter
import os
import re





reader = PdfReader("./import/example.pdf")
number_of_pages = len(reader.pages)
for idx, r in enumerate(reader.pages):
    text = r.extract_text()
    text_part = re.search('Kundennummer: ([0-9]{7})', text)
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(reader.getPage(idx))
    output = f'./export/dateiname_{text_part.group(1)}_{idx}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
# page = reader.pages[0]
# text = page.extract_text()