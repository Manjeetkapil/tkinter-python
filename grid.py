from tkinter import *

root = Tk()

mylabel1 = Label(root,text="Packing it ").grid(row=0,column=0)
mylabel2 = Label(root, text ="Second Label")
mylabel3 = Label(root, text ="Thirf Label")
mylabel4 = Label(root, text ="Fourth Label")
mylabel5 = Label(root, text ="Fifth Label")

mylabel2.grid(row=1,column=1)
mylabel3.grid(row=2,column=2)
mylabel4.grid(row=3,column=3)
mylabel5.grid(row=4,column=4)

root.mainloop()