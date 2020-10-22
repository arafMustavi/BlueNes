from pdflatex import PDFLaTeX

pdfl = PDFLaTeX.from_texfile("main.tex")
# print(pdfl)
pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)