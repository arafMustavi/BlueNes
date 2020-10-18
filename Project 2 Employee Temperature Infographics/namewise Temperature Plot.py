# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("HRProject_Temp_dummydata.xlsx")

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
for i in range(sheet.nrows):
    dataset.append(sheet.row_values(i))

print(dataset)

name = input("Enter Name for the Employee").lower()
# startdate = input("Date From:")
# enddate = input("Date To:")
# daterange = (startdate,enddate)


# Data Plot

import matplotlib.pyplot as plt


# def plot_data(in_values, out_values, name):  # ,n,p,color):
#     plt.plot(,color = '')
#     plt.plot(in_values)
#
#     plt.plot(out_values)
#     plt.xlabel('Date')
#     plt.ylabel('Temperature')
#     plt.title('Temperature Graph for : ' + str(name))
#     plt.show()

def plot_data(in_values, out_values,normal_line, name):
    # fig, ax = plt.subplots()
    # ax.set_color_cycle(['green', 'red'])
    plt.plot(in_values, label='In Temp', color='g')
    plt.plot(out_values, label='Out Temp', color='b')
    plt.plot(normal_line, label='Normal Temp', color='r')
    plt.legend(loc='best')
    plt.title('Temperature Graph for : ' + str(name))
    plt.show()


# x = np.linspace(0, 1, 10)
# for i in range(1, 6):
#     plt.plot(x, i * x + i, label='$y = {i}x + {i}$'.format(i=i))


# Fetch Temperature Data
in_values = []
out_values = []
normal_line = []
# name = dataset[1][0]
for i in range(rows):
    if dataset[i][2].lower() == name:
        # x_values.append(dataset[i][2]-dataset[2][2])
        #     x_values.append(i)
        normal_line.append(37)
        in_values.append(dataset[i][6])
        out_values.append(dataset[i][9])

plot_data(in_values, out_values,normal_line, name)
