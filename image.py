from tkinter import *
from PIL import ImageTk,Image
import requests
import asyncio
import time

root = Tk()

root.title('Image viewer')
# root.iconbitmap("@potato.xbm")
response = requests.get("https://source.unsplash.com/1100x600/?tech,laptop,nature")

file = open("sam.jpeg", "wb")
file.write(response.content)
file.close()
my_img = ImageTk.PhotoImage(Image.open("sam.jpeg"))

my_label = Label(image=my_img)

my_label.grid(row=0,column=0)

async def get2():
	response = requests.get("https://source.unsplash.com/1100x600/?tech,laptop,nature")
	file = open("sam.jpeg", "wb")
	file.write(response.content)
	file.close()

async def get():
	await get2()
	# return response

def nex():
	global root
	root.quit() #only works with root.quit() perfectly and can work not so good with root.withdraw()
	# root = Tk()
	# root.title('Image viewer')
	loop = asyncio.get_event_loop()
	loop.run_until_complete(get())
	k_img = ImageTk.PhotoImage(Image.open("sam.jpeg"))
	my_label = Label(image=k_img)
	my_label.grid(row=0,column=0)
	print('noooooo\n')
	# root.deiconify() if you want to use root.withdraw()
	root.mainloop()
	# root.destroy()

button_quit = Button(root,text="Exit", command=root.destroy)
button_quit.grid(row=1,column=0)
button_next = Button(root,text="Next",command=nex)
button_next.grid(row=1,column=1)
root.mainloop()