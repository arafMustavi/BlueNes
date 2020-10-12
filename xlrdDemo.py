# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("dummydata.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0, 0))

# Print the number of column and row
print(sheet.ncols)
print(sheet.nrows)

# Iterate through the rows and Columns
columns = sheet.ncols
rows = sheet.nrows

dataset = []
for i in range(rows):
    row_data = []
    for j in range(columns):
        row_data.append(sheet.cell_value(i, j))
        # print(sheet.cell(i, j))  # Prints the cells in the format 'type' : 'value'
        # print(sheet.cell_value(i, j))  # Prints the value in the particular cells
    dataset.append(row_data)

print(dataset)

# Prints the data row by row | The sheet.row_value(x) returns the sheet as a list
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))
#     # print(type(sheet.row_values(i)))

# Prints the data row by Columns | The sheet.col_values(x) returns the sheet columns as a list
# for i in range(sheet.ncols):
#     print(sheet.col_values(i))
