import tkinter as tk


def show_entry_fields():
    print("username: %s\npassword: %s" % (e1.get(), e2.get()))


master = tk.Tk()
tk.Label(master, text="username").grid(row=0)
tk.Label(master, text="password").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


def hello():
    show_text = "Welcome" + str(e1)
    label1 = tk.Label(master, text=show_text, fg='green', font=('helvetica', 12, 'bold'))
    master.create_window(150, 200, window=label1)


tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Login', command=hello).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
