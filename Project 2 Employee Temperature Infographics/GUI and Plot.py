import tkinter as tk
import matplotlib.pyplot as plt
import xlrd

rows = 0


#######################################
def excel_to_list(loc):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows

    dataset = []
    for i in range(rows):
        dataset.append(sheet.row_values(i))
    return dataset


def plot_data(in_values, out_values, normal_line, id, name):
    # fig, ax = plt.subplots()
    # ax.set_color_cycle(['green', 'red'])
    plt.plot(in_values, label='In Temp', color='g')
    plt.plot(out_values, label='Out Temp', color='b')
    plt.plot(normal_line, label='Normal Temp', color='r')
    plt.legend(loc='best')
    plt.title('Temperature Graph for : ' + str(id) + str(name))
    plt.show()


def dataset_to_names(dataset):
    employee_names = []
    for i in dataset[3:]:
        # employee_names.append( str(int(i[1])) + str(i[2]))
        employee_names.append(i[2])
    employee_names = list(set(employee_names))
    return employee_names


#######################################


loc = ("HRProject_Temp_dummydata.xlsx")
dataset = excel_to_list(loc)
print(dataset)
dataset_to_names(dataset)
####################################################
Employee_names = dataset_to_names(dataset)
MODES = [tk.SINGLE, tk.BROWSE, tk.MULTIPLE, tk.EXTENDED]

selected = []
class ListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.list = tk.Listbox(self)
        self.list.insert(0, *Employee_names)
        self.print_btn = tk.Button(self, text="Show Demographic Chart",
                                   command=self.print_selection)
        self.btns = [self.create_btn(m) for m in MODES]

        self.list.pack()
        self.print_btn.pack(fill=tk.BOTH)
        for btn in self.btns:
            btn.pack(side=tk.LEFT)

    def create_btn(self, mode):
        cmd = lambda: self.list.config(selectmode=mode)
        return tk.Button(self, command=cmd,
                         text=mode.capitalize())

    def print_selection(self):
        selection = self.list.curselection()
        print([self.list.get(i) for i in selection])
        # selected = [self.list.get(i) for i in selection]
        # print(selected)
        # return [self.list.get(i) for i in selection]


if __name__ == "__main__":
    app = ListApp()
    # selected = app.print_selection()
    # print(selected)
    app.mainloop()


###########################################################

print(selected)
# name = dataset[1][0]
# Fetch Temperature Data
id = int(input("Enter ID for the Employee"))
in_values = []
out_values = []
normal_line = []
name = ''
print(dataset)
rows = len(dataset)
for i in range(rows):
    print(i)
    if (dataset[i][1]) == id:
        name = dataset[i][2]
        normal_line.append(37)
        in_values.append(dataset[i][6])
        out_values.append(dataset[i][9])
        # x_values.append(dataset[i][2]-dataset[2][2])
        #     x_values.append(i)

print(in_values)
print(out_values)
plot_data(in_values, out_values, normal_line, id, name)
