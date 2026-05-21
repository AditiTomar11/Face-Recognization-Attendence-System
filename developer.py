from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os




class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="DEVELOPER", bg="white", fg="blue", font=("Helvetica", 35, "bold"))
        title_lbl.place(relx=0.5, rely=0.03, width=1540, height=45, anchor=CENTER)

        img_top = Image.open(r"Image_1\developer.jpg")
        img_top = img_top.resize((1530,720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Main Frame
        main_frame=Frame(f_lbl,bd=2,bg = "white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1 = Image.open(r"Image_1\developer.jpg")
        img_top1 = img_top1.resize((200,200))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top)

        f_lbl = Label(main_frame, image=self.photoimg_top)
        f_lbl.place(x=300, y=0, width=200, height=200)


        # Developer info
        dp_label=Label(main_frame,text="Hello My Name is Aditi Tomar",font=("Helvetica",13,"bold"),bg="white")
        dp_label.place(x=0,y=5)

        dp_label=Label(main_frame,text="I am a developer of this project",font=("Helvetica",13,"bold"),bg="white")
        dp_label.place(x=0,y=40)

        # Third Image
        img14 = Image.open(r"Image_1\14.jpg")
        img14 = img14.resize((500, 400))  # Adjusted width to 500
        self.photoimg14 = ImageTk.PhotoImage(img14)
            
        f_lbl3 = Label(main_frame, image=self.photoimg14)
        f_lbl3.place(x=0, y=210, width=500, height=400)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()