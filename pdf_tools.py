import os
from PyPDF2 import PdfWriter, PdfReader
from img2pdf import convert
from io import BytesIO

def createPDF(paths:list[str], output):
    output = 'PDF_combinado.pdf'
    pdf_writer = PdfWriter()
    pdf_ = False
    for path in paths:
        if path.endswith('.jpg') or path.endswith('.png') or path.endswith('.jpeg'):
            # Convertir la imagen a PDF en memoria
            pdf = BytesIO(convert(path))
        elif path.endswith('.pdf'):
            pdf = path
        else:
            continue
        pdf_ = True
        pdf_reader = PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    if not pdf_: return
    with open(output, 'wb') as out_file:
        pdf_writer.write(out_file)

    # Abrir el archivo PDF
    os.startfile(output)