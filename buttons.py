from tkinter import *

root = Tk()

def myClick():
	myLable = Label(root,text="hi")
	myLable.pack()

myButton = Button(root, text="click it",padx=20,pady=20,command=myClick,fg="blue",bg="green")
''' 
padx is coordinate x length = width of button
pady cordibnate y length of y-axis = height of button
command is calling a funtion(note: without parenthesis)
fg = button text color
bg = button background colour
Button() for defining new button
'''
myButton.pack()

root.mainloop()