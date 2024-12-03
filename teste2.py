from tkinter import *
import PIL.ImageTk
import PIL.Image
root = Tk()
#open image
logo1=PIL.Image.open("Imagens\image_background.png")
#resize
resized = logo1.resize((250,160),PIL.Image.ANTIALIAS)
new_pic = PIL.ImageTk.PhotoImage(resized)
logo_label = Tk.Label(root,image = new_pic)
logo_label.grid(row=0,column=0)

root.mainloop()