# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("dummydata.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


# Print the number of column and row
print(sheet.ncols)
print(sheet.nrows)

# Iterate through the rows and Columns
columns = sheet.ncols
rows = sheet.nrows

dataset = []
# Appends the data row by row | The sheet.row_value(x) returns the sheet as a list
for i in range(1,sheet.nrows):
    dataset.append(sheet.row_values(i))

print(dataset)


# Data Plot

import matplotlib.pyplot as plt
def plot_data(x_values,y_values):#,n,p,color):
  plt.plot(x_values, y_values)
  plt.xlabel('Date')
  plt.ylabel('Temperature')
  plt.title('Temperature Data')
  plt.show()

# Fetch Temperature Data
y_values = []
x_values = []
for i in range(rows-1):
  x_values.append(i)
  y_values.append(dataset[i][3])

plot_data(x_values, y_values)
