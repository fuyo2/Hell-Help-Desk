from tkinter import *

from tkinter import messagebox

from PIL import Image, ImageTk

root = Tk()

root.title ("Hell Help Desk")
root.geometry("640x420")

app = Frame(root)
app.grid()
app.place(relx=.5, rely=.5, anchor="center")

menu = Menu(app.master)
app.master.config(menu=menu)
    
file = Menu(menu)
file.add_command(label='Save')
file.add_command(label='Exit', command=root.destroy)
menu.add_cascade(label='File', menu=file)

edit = Menu(menu)
edit.add_command(label='Undo')
edit.add_command(label='Redo')
menu.add_cascade(label='Edit', menu=edit)

logo = Image.open('logo.png')
render = ImageTk.PhotoImage(logo)

img = Label(app, image=render)
img.image = render
img.place(x=0,y=0)
img.grid(row=1, column=1, padx=5, pady=5)

nameLabel = Label(app, text="Name:",font=12)
nameLabel.grid(row=2, column=1, padx=5, pady=5)

nameEntry = Entry(app, font=12, width=20)
nameEntry.grid(row=3, column=1, padx=5, pady=5)

deptLabel = Label(app, text="Department:",font=12)
deptLabel.grid(row=4, column=1, padx=1, pady=5)

deptEntry = Entry(app, font=12, width=20)
deptEntry.grid(row=5, column=1, padx=5, pady=5)

descptLabel = Label(app, text="Description of issue:",font=12)
descptLabel.grid(row=6, column=1, padx=1, pady=5)

descptEntry = Entry(app, font=12, width=20)
descptEntry.grid(row=7, column=1, padx=5, pady=5)

def dialog():
    var = messagebox.showinfo("Case Submitted" , "Your ticket has been successfully submitted, It will never be reviewed.")
submitButton = Button(app, font=12, text = "Submit Ticket", height = 1, width = 20, command=dialog)
submitButton.grid(row=8, column=1, padx=5, pady=5)

def dialog2():
    var = messagebox.showinfo("Case Submitted" , "You will never be able to modify your case.")
ExCaseButton = Button(app, font=12, height = 1, width = 20)
ExCaseButton.grid(row=9, column=1, padx=5, pady=5)
ExCaseButton.configure(text = "Modify Existing Case", command=dialog2)

quitButton = Button(app, font=12, text="QUIT", fg="red", command=root.destroy, height = 1, width = 20,)
quitButton.grid(row=10, column=1, padx=5, pady=5)

root.mainloop()


