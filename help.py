from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os




class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="HELP", bg="white", fg="blue", font=("Helvetica", 35, "bold"))
        title_lbl.place(relx=0.5, rely=0.03, width=1540, height=45, anchor=CENTER)

        img_top = Image.open(r"Image_1\Help.png")
        img_top = img_top.resize((1530,720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)


        # Developer info
        dp_label=Label(f_lbl,text="Email:vloggertrain@gmail.com",font=("Helvetica",13,"bold"),bg="white")
        dp_label.place(x=650,y=425)

        


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()