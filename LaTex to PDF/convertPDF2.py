import os
import pdflatex
import jinja2

env = pdflatex.JINJA2_ENV
env['loader'] = jinja2.FileSystemLoader(os.path.abspath('.'))
env = jinja2.Environment(**env)
template = env.get_template('main.tex')
pdfl = pdflatex.PDFLaTeX.from_jinja2_template(template, data='Hello world!')
pdf, log, cp = pdfl.create_pdf()