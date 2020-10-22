import pdflatex

with open('main.tex', 'rb') as f:
    pdfl = pdflatex.PDFLaTeX.from_binarystring(f.read(), 'main')
pdf, log, cp = pdfl.create_pdf()