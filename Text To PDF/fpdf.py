# Python program to create 
# a pdf file 


import fpdf

# save FPDF() class into a  
# variable pdf 
pdf = fpdf.FPDF()

# Add a page 
pdf.add_page()

# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size=15)

# create a cell 
pdf.cell(200, 10, txt="NESTernship", ln=1, align='C')

# add another cell 
pdf.cell(200, 10, txt="Medical Expense Records for the month of November 2020.",
         ln=2, align='C')

# save the pdf with name .pdf 
pdf.output("Report.pdf")
