from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk

import datetime

import csv

import tkinter

root = Tk()
# Window title
root.title("Hell Help Desk")
# Window size.
root.geometry("640x480")
# Window icon.
root.iconbitmap('favicon.ico')
# root.configure(background='')

today = datetime.date.today()


def retrieveInput():
    inputName = nameEntry.get()
#    print(inputName)


def saveInput():
    # Collects user input from text boxes and makes it a veriable
    inputName = nameEntry.get()
    inputDept = deptEntry.get()
    inputDescpt = descptEntry.get()

    # Opens and writes values of text boxes to a CSV file.
    with open("output_data.csv", "a") as outFile:
        outString = str(inputName)
        outString += " , " + str(inputDept)
        outString += " , " + str(inputDescpt)
        outString += " , " + str(today)
        outString += "\n"
        outFile.write(outString)

# About window under Help menu.


def aboutWindow():
    root = Tk()
    # Window title
    root.title("About - Hell Help Desk")
    # Window size.
    root.geometry("320x210")
    # Window icon.
    root.iconbitmap('favicon.ico')

    app = Frame(root)
    app.grid()
    app.place(relx=.5, rely=.5, anchor="center")

    # Text label
    topLabel = Label(app, text="Made by:", font=12)
    topLabel.grid(row=2, column=1, padx=5, pady=5)

    dateLabel = Label(app, text="Justin Cole 2018", font=12)
    dateLabel.grid(row=3, column=1, padx=5, pady=5)

    versionLabel = Label(app, text="version 0.03", font=12)
    versionLabel.grid(row=4, column=1, padx=5, pady=5)

    # Quits out of the About window
    okButton = Button(app, font=12, text="Ok", fg="black",
                      command=root.destroy, height=1, width=20,)
    okButton.grid(row=10, column=1, padx=5, pady=5)

    # Keeps the window in a loop to not close until okButton in pressed.
    root.mainloop()

# Modify Existing Case window


def modifyWindow():
    root = Tk()
    # Window title
    root.title("Modify Existing Case - Hell Help Desk")
    # Window size.
    root.geometry("472x640")
    # Window icon.
    root.iconbitmap('favicon.ico')

    app = Frame(root)
    app.grid()
    app.place(relx=.5, rely=.5, anchor="center")

#    topLabel = Label(app, text="Open Cases",font=12)
#    topLabel.grid(row=1, column=1, padx=5, pady=5)

    with open("output_data.csv", newline="") as file:
        reader = csv.reader(file)

        # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                labelCSV = tkinter.Label(root, width=16, height=2, text=row, relief=tkinter.RIDGE)
                labelCSV.grid(row=r, column=c)
                c += 1
            r += 1

    # Quits out of the About window
    okButton = Button(app, font=12, text="Close", fg="black",
                      command=root.destroy, height=1, width=20,)
    okButton.grid(row=10, column=1, padx=5, pady=5)


app = Frame(root)
app.grid()
app.place(relx=.5, rely=.5, anchor="center")

# Menu bar.
menu = Menu(app.master)
app.master.config(menu=menu)

file = Menu(menu)
file.add_command(label='Save', command=saveInput)
file.add_command(label='Exit', command=root.destroy)
menu.add_cascade(label='File', menu=file)

edit = Menu(menu)
edit.add_command(label='Undo')
edit.add_command(label='Redo')
menu.add_cascade(label='Edit', menu=edit)

help = Menu(menu)
help.add_command(label='About', command=aboutWindow)
menu.add_cascade(label='Help', menu=help)

# Image used as the logo in the main window.
logo = Image.open('logo.png')
render = ImageTk.PhotoImage(logo)

img = Label(app, image=render)
img.image = render
img.place(x=0, y=0)
img.grid(row=1, column=1, padx=5, pady=5)

# Text boxes and labels for the text boxes.
nameLabel = Label(app, text="Name:", font=12)
nameLabel.grid(row=2, column=1, padx=5, pady=5)

nameEntry = Entry(app, font=12, width=20)
nameEntry.grid(row=3, column=1, padx=5, pady=5)

deptLabel = Label(app, text="Department:", font=12)
deptLabel.grid(row=4, column=1, padx=1, pady=5)

deptEntry = Entry(app, font=12, width=20)
deptEntry.grid(row=5, column=1, padx=5, pady=5)

descptLabel = Label(app, text="Description of issue:", font=12)
descptLabel.grid(row=6, column=1, padx=1, pady=5)

descptEntry = Entry(app, font=12, width=20)
descptEntry.grid(row=7, column=1, padx=5, pady=5)


def dialog():
    saveInput()
    var = messagebox.showinfo(
        "Case Submitted", "Your ticket has been successfully submitted, It will never be reviewed.")


# This is the subit button.
submitButton = Button(app, font=12, text="Submit Ticket", height=1, width=20, command=dialog)
submitButton.grid(row=8, column=1, padx=5, pady=5)


def dialog2():
    var = messagebox.showinfo("Case Submitted", "You will never be able to modify your case.")


# This is the Modify Existing Case button
ExCaseButton = Button(app, font=12, height=1, width=20)
ExCaseButton.grid(row=9, column=1, padx=5, pady=5)
ExCaseButton.configure(text="Modify Existing Case", command=modifyWindow)

# This is the QUIT button.
quitButton = Button(app, font=12, text="QUIT", fg="red", command=root.destroy, height=1, width=20,)
quitButton.grid(row=10, column=1, padx=5, pady=5)

# Keeps the program running in a loop until it is terminated by the user.
root.mainloop()
