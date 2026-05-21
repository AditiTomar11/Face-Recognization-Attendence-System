from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from face_module import Face_Recognition
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # FIRST Image
        img1 = Image.open(r"Image_1\1.jpg")
        img1 = img1.resize((500, 150))  # Adjusted width to 500
        self.photoimg1 = ImageTk.PhotoImage(img1)
            
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=140)
            
        # Second Image
        img2 = Image.open(r"Image_1\2.jpg")
        img2 = img2.resize((520, 150))  # Adjusted width to 500
        self.photoimg2 = ImageTk.PhotoImage(img2)
            
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=520, height=140)  # Adjusted x to 500
            
        # Third Image
        img3 = Image.open(r"Image_1\3.jpg")
        img3 = img3.resize((540, 150))  # Adjusted width to 500
        self.photoimg3 = ImageTk.PhotoImage(img3)
            
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=540, height=140)  # Adjusted x to 1000
            
        # background image
        img4 = Image.open(r"Image_1\4.jpg")
        img4 = img4.resize((1550, 900))  # Adjusted width to 1530 and height to 600
        self.photoimg4 = ImageTk.PhotoImage(img4)
            
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1550, height=700)  # Adjusted y to 130 and height to 600
            
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE" ,fg="red", font=("Helvetica", 35, "bold"))
        title_lbl.place(relx=0.5, rely=0.03,width=1540,height=45, anchor=CENTER)  # Centered the label

        # ==============time===============
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

            lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='red')
            lbl.place(x=10,y=0,width=150,height=50)
            time()
        
        # student button
        img5 = Image.open(r"Image_1\5.jpg")
        img5 = img5.resize((320, 240))
        self.photoimg5 = ImageTk.PhotoImage(img5)
            
        b1 = Button(bg_img, image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2" ,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=200, y=280, width=220, height=40)
        
        
        # detect face button
        img6 = Image.open(r"Image_1\6.jpg")
        img6 = img6.resize((320, 240))
        self.photoimg6 = ImageTk.PhotoImage(img6)
            
        b1 = Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Face Detector" ,cursor="hand2",command=self.face_data,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=500, y=280, width=220, height=40)
        
        # Attendance button
        img7 = Image.open(r"Image_1\7.jpg")
        img7 = img7.resize((320, 240))
        self.photoimg7 = ImageTk.PhotoImage(img7)
            
        b1 = Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.attendance)
        b1.place(x=800, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Attendance" ,cursor="hand2",command=self.attendance,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=800, y=280, width=220, height=40)
        
        
        # Help/Support button
        img8 = Image.open(r"Image_1\8.jpg")
        img8 = img8.resize((320, 240))
        self.photoimg8 = ImageTk.PhotoImage(img8)
            
        b1 = Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Help/Support" ,cursor="hand2",command=self.help_data,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=1100, y=280, width=220, height=40)
        
        # Train Face button
        img9 = Image.open(r"Image_1\9.jpg")
        img9 = img9.resize((320, 240))
        self.photoimg9 = ImageTk.PhotoImage(img9)
            
        b1 = Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Train Data" ,cursor="hand2",command=self.train_data,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=200, y=580, width=220, height=40)
        
        
        # photos face button
        img10 = Image.open(r"Image_1\10.jpg")
        img10 = img10.resize((320, 240))
        self.photoimg10 = ImageTk.PhotoImage(img10)
            
        b1 = Button(bg_img, image=self.photoimg10,cursor = "hand2" , command=self.open_img)
        b1.place(x=500, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Photos" , cursor = "hand2" , command=self.open_img,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=500, y=580, width=220, height=40)
        
        # Developer button
        img11 = Image.open(r"Image_1\11.jpg")
        img11 = img11.resize((320, 240))
        self.photoimg11 = ImageTk.PhotoImage(img11)
            
        b1 = Button(bg_img, image=self.photoimg1,cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Developer" ,cursor="hand2",command=self.developer_data,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=800, y=580, width=220, height=40)
        
        
        #Exit button
        img12 = Image.open(r"Image_1\12.jpg")
        img12 = img12.resize((320, 240))
        self.photoimg12 = ImageTk.PhotoImage(img12)
            
        b1 = Button(bg_img, image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1100, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Exit" ,cursor="hand2",command=self.iExit,bg="darkblue",fg="white", font=("Helvetica", 15, "bold"))
        b1_1.place(x=1100, y=580, width=220, height=40)
        
    
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return



# ================ Functions Button ==================
    def student_details(self):
        self.new_Window=Toplevel(self.root)
        self.app=Student(self.new_Window)


    def train_data(self):
        self.new_Window=Toplevel(self.root)
        self.app=Train(self.new_Window)



    def face_data(self):
        self.new_Window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_Window)
    
    def attendance(self):
        self.new_Window=Toplevel(self.root)
        self.app=Attendance(self.new_Window)

    def developer_data(self):
        self.new_Window=Toplevel(self.root)
        self.app=Developer(self.new_Window)

    def help_data(self):
        self.new_Window=Toplevel(self.root)
        self.app=Developer(self.new_Window)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
