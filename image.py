from tkinter import *
from PIL import ImageTk,Image
import requests

root = Tk()

root.title('Image viewer')
# root.iconbitmap("@potato.xbm")
response = requests.get("https://source.unsplash.com/1100x600/?tech,laptop,nature")

file = open("sam.jpeg", "wb")
file.write(response.content)
file.close()
my_img = ImageTk.PhotoImage(Image.open("sam.jpeg"))

my_label = Label(image=my_img)

my_label.pack()

button_quit = Button(root,text="Exit", command=root.quit)
button_quit.pack()
root.mainloop()