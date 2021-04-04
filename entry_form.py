from tkinter import *

root = Tk()

e = Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()
e.insert(0,"xx")
'''
e = form input same as html
e.get() to get value inside the form currently we calling button from myclick() funtion
e.insert(0,"put default text inside form")
'''
def myClick():
	hello = "hello " + e.get()
	myLable = Label(root,text=hello)
	myLable.pack()

myButton = Button(root, text="click it",padx=20,pady=20,command=myClick,fg="blue",bg="green")

myButton.pack()

root.mainloop()