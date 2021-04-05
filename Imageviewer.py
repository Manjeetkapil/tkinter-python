import os
from os import listdir
from os.path import isfile, join
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/images"
from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title('Image viewer')
# root.iconbitmap("@potato.xbm")
files = [f for f in listdir(ROOT_DIR) if isfile(join(ROOT_DIR, f))]
print(files)
image_list = []
for i in files:
	my_img = ImageTk.PhotoImage(Image.open("images/"+i))
	image_list.append(my_img)

# for i in image_list
number = 0
my_label = Label(image=image_list[number])
my_label.grid(row=0,column=0,columnspan=3)

# my_label.pack()
def forward(image_number):
	global my_label
	global number
	global image_list
	my_label.grid_forget()
	number = (number + 1)%len(image_list)
	my_label = Label(image=image_list[number])
	my_label.grid(row=0,column=0,columnspan=3)

def back():
	global my_label
	global number
	global image_list
	my_label.grid_forget()
	if number>0:
		number = number -1
	else:
		number = len(image_list)-1
	my_label = Label(image=image_list[number])
	my_label.grid(row=0,column=0,columnspan=3)

button_back = Button(root,text="<<",command=lambda:back())
button_quit = Button(root,text="Exit Program", command=root.quit)
button_forward = Button(root,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
# button_quit.pack()
root.mainloop()