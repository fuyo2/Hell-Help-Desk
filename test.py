from tkinter import *

from tkinter import messagebox
import tkinter
import csv

root = tkinter.Tk()

app = Frame(root)
app.grid()
app.place(relx=.5, rely=.5, anchor="center")

# open file
with open("output_data.csv", newline = "") as file:
    reader = csv.reader(file)

   # r and c tell us where to grid the labels

         # i've added some styling
    label = tkinter.Label(root, width = 10, height = 2, text = row, relief = tkinter.RIDGE)
    label.grid(row = 1, column = 1)


root.mainloop()
