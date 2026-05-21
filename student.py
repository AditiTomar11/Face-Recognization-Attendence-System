from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


if not os.path.exists("data"):
    os.makedirs("data")

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        # =================== Variables =====================
        self.var_dp = StringVar()
        self.var_course=StringVar()

        self.var_year=StringVar()

        self.var_semester=StringVar()

        self.var_std_id=StringVar()

        self.var_std_name=StringVar()

        self.var_div=StringVar()

        self.var_roll=StringVar()

        self.var_gender=StringVar()

        self.var_dob=StringVar()

        self.var_email=StringVar()

        self.var_phone=StringVar()

        self.var_address=StringVar()

        self.var_teacher=StringVar()

        
        # FIRST Image
        img13 = Image.open(r"D:\face_recognition\Image_1\13.jpg")
        img13 = img13.resize((500, 150))  # Adjusted width to 500
        self.photoimg13 = ImageTk.PhotoImage(img13)
            
        f_lbl1 = Label(self.root, image=self.photoimg13)
        f_lbl1.place(x=0, y=0, width=500, height=140)
            
        # Second Image
        img15 = Image.open(r"D:\face_recognition\Image_1\15.jpg")
        img15 = img15.resize((520, 150))  # Adjusted width to 500
        self.photoimg15 = ImageTk.PhotoImage(img15)
            
        f_lbl2 = Label(self.root, image=self.photoimg15)
        f_lbl2.place(x=500, y=0, width=520, height=140)  # Adjusted x to 500
            
        # Third Image
        img14 = Image.open(r"D:\face_recognition\Image_1\14.jpg")
        img14 = img14.resize((540, 150))  # Adjusted width to 500
        self.photoimg14 = ImageTk.PhotoImage(img14)
            
        f_lbl3 = Label(self.root, image=self.photoimg14)
        f_lbl3.place(x=1000, y=0, width=540, height=140)  # Adjusted x to 1000
            
        
        # background image
        img4 = Image.open(r"D:\face_recognition\Image_1\4.jpg")
        img4 = img4.resize((1550, 900))  # Adjusted width to 1530 and height to 600
        self.photoimg4 = ImageTk.PhotoImage(img4)
            
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1550, height=700)  # Adjusted y to 130 and height to 600
            
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM " ,bg="green",fg="white", font=("Helvetica", 35, "bold"))
        title_lbl.place(relx=0.5, rely=0.03, width=1540,height=45, anchor=CENTER)  # Centered the label
        
        # Main Frame
        main_frame=Frame(bg_img,bd=2,bg = "white")
        main_frame.place(x=25,y=60,width=1490,height=600)
        
        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Helvetica",15,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)
        
        imgStL1 = Image.open(r"D:\face_recognition\Image_1\StL1.jpg")
        imgStL1 = imgStL1.resize((820, 150))  # Adjusted width to 500
        self.photoimgStL1 = ImageTk.PhotoImage(imgStL1)
            
        f_lbl1 = Label(Left_frame, image=self.photoimgStL1)
        f_lbl1.place(x=0, y=0, width=719, height=140)
        
        # current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("Helvetica",13,"bold"))
        current_course_frame.place(x=5,y=140,width=710,height=110)
        
        #Department
        dp_label=Label(current_course_frame,text="Department",font=("Helvetica",13,"bold"),bg="white")
        dp_label.grid(row=0,column=0,padx=10)
        
        dp_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dp ,font=("Helvetica",13,"bold") , state="readonly")
        dp_combo["values"]=("Select Department","CSE","IT","AIML","Civil","Mechanical","Electronics","Agriculture")
        dp_combo.current(0)
        dp_combo.grid(row=0,column=1,padx=2,pady=10)
        
        #Course
        course_label=Label(current_course_frame, text="Course",font=("Helvetica",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Helvetica",13,"bold") , state="readonly")
        course_combo["values"]=("Select Course","B.Tech","MBA","MCA","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_label=Label(current_course_frame,text="Year",font=("Helvetica",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Helvetica",13,"bold") , state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("Helvetica",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("Helvetica",13,"bold") , state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # Class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("Helvetica",13,"bold"))
        class_student_frame.place(x=0,y=255,width=715,height=295)
        
        #StudentID
        semester_label=Label(class_student_frame,text="StudentID:",font=("Helvetica",13,"bold"),bg="white")
        semester_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("Helvetica",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Class Division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("Helvetica",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Helvetica",13,"bold") , state="readonly")
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #roll no
        roll_no_label=Label(class_student_frame,text="Roll No.:",font=("Helvetica",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("Helvetica",13,"bold"),bg="white")
        gender_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        # gender_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Helvetica",13,"bold") , state="readonly")
        gender_combo["values"]=("Male","Female","Other","Not To Disclose")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)
        
        #email id
        email_label=Label(class_student_frame,text="Email:",font=("Helvetica",13,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=6,sticky=W)
        
        #phone No
        phone_label=Label(class_student_frame,text="Phone No.:",font=("Helvetica",13,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label=Label(class_student_frame,text="Address:",font=("Helvetica",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("Helvetica",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(class_student_frame,text="Date of birth:",font=("Helvetica",13,"bold"),bg="white")
        dob_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio1,text="take Photo Sample",value="Yes",variable=self.var_radio1)
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio1,text="No Photo Sample",value="No",variable=self.var_radio1)
        radiobtn2.grid(row=6,column=1)
        
        # Button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=710,height=50)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="indigo",fg="white")
        reset_btn.grid(row=0,column=3)
        
        # Button Frame
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="black")
        btn_frame1.place(x=0,y=235,width=710,height=40)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="orange",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="purple",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        
        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Helvetica",15,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        img_right = Image.open(r"D:\face_recognition\Image_1\StL1.jpg")
        img_right = imgStL1.resize((820, 150))  # Adjusted width to 500
        self.photoimg_right = ImageTk.PhotoImage(imgStL1)
            
        f_lbl1 = Label(Right_frame, image=self.photoimg_right)
        f_lbl1.place(x=0, y=0, width=719, height=140)
        
        # ========Search Style========
        Search_frame=LabelFrame(Right_frame,bd=3,relief=RIDGE,text="Search System",font=("Helvetica",13,"bold"))
        Search_frame.place(x=0,y=135,width=715,height=70)
        
        search_label=Label(Search_frame,text="Search By:",font=("Helvetica",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("Helvetica",13,"bold") , state="readonly",width=15)
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="LimeGreen",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="DeepPink",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        # ==========table frame====
        table_frame=Frame(Right_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=210,width=715,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll_no","gender","dob","email","phone_no","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll_no",text="Roll_No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone_no", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # ================ Function Declaration =============
    def add_data(self):
        if self.var_dp.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ayodhya2024@",database="face_recognizzer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dp.get(),
                    self.var_course.get(),
                    self.var_year.get(), 
                    self.var_semester.get(),
                    self.var_std_id.get(), 
                    self.var_std_name.get(), 
                    self.var_div.get(), 
                    self.var_roll.get(), 
                    self.var_gender.get(), 
                    self.var_dob.get(), 
                    self.var_email.get(), 
                    self.var_phone.get(), 
                    self.var_address.get(),
                    self.var_teacher.get(), 
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been recorded",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


                # =================fetch data============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ayodhya2024@",database="face_recognizzer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        # ===============get cursor==================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dp.set(data[0]),

        self.var_course.set(data[1]),

        self.var_year.set(data[2]),

        self.var_semester.set(data[3]),

        self.var_std_id.set(data[4]),

        self.var_std_name.set(data[5]),

        self.var_div.set(data[6]),

        self.var_roll.set(data[7]),

        self.var_gender.set(data[8]),

        self.var_dob.set(data[9]),

        self.var_email.set(data[10]),

        self.var_phone.set(data[11]),

        self.var_address.set(data[12]),

        self.var_teacher.set(data[13]),

        self.var_radio1.set(data[14])

        # update function
    def update_data(self):
        if self.var_dp.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to updates this student details",parent=self.root)
                if update > 0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ayodhya2024@",database="face_recognizzer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET department=%s, course=%s, year=%s, semester=%s, Name=%s, Division=%s,  Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE student_id=%s",(
                    self.var_dp.get(),
                    self.var_course.get(),
                    self.var_year.get(), 
                    self.var_semester.get(), 
                    self.var_std_name.get(), 
                    self.var_div.get(), 
                    # self.var_roll.get(),
                    self.var_gender.get(), 
                    self.var_dob.get(), 
                    self.var_email.get(), 
                    self.var_phone.get(), 
                    self.var_address.get(),
                    self.var_teacher.get(), 
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))
                
                else:
                    if not update:
                        return
                messagebox.showinfo("Success" , "Students details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #  delete function 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student ",parent=self.root)
                if delete > 0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ayodhya2024@",database="face_recognizzer")
                    my_cursor=conn.cursor()
                    sql = "delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ConnectionResetError
    def reset_data(self):
        self.var_dp.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")  # Fixed the typo here
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

# ===================== Generate Data set or take photo samples ===========
    def generate_dataset(self):
        if self.var_dp.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ayodhya2024@",database="face_recognizzer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE student SET department=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE student_id=%s",(
                    self.var_dp.get(),
                    self.var_course.get(),
                    self.var_year.get(), 
                    self.var_semester.get(), 
                    self.var_std_name.get(), 
                    self.var_div.get(), 
                    # self.var_roll.get(), 
                    self.var_gender.get(), 
                    self.var_dob.get(), 
                    self.var_email.get(), 
                    self.var_phone.get(), 
                    self.var_address.get(),
                    self.var_teacher.get(), 
                    self.var_radio1.get(),
                    self.var_std_id.get() # == id +1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # =========== load predefined data on face frontals from opencv ==========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factors = 1.3
                    # minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    return None
                    
                cap = cv2.VideoCapture(0)

                #new 
                if not cap.isOpened():
                    messagebox.showerror("Error", "Camera not accessible!")
                    return


                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                    face = cv2.resize(face_cropped(my_frame),(450,450))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Croppped Face ",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 30:
                        break


                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set completed !!!!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
