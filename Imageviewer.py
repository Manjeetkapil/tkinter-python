from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('Image viewer')
# root.iconbitmap("@potato.xbm")
my_img = ImageTk.PhotoImage(Image.open("potato.jpg"))

my_label = Label(image=my_img)

my_label.pack()

button_quit = Button(root,text="Exit", command=root.quit)
button_quit.pack()
root.mainloop()