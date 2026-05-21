from tkinter import *
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from PIL import Image, ImageTk
import os
import csv

if not os.path.exists("data"):
    os.makedirs("data")

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_atten_status = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar() # Added
        self.var_atten_date = StringVar() # Added

        # Initialize the time and date immediately
        self.fetch_system_time()

        # Images
        self.setup_images()

        # Background and Title
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1550, height=700)
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", bg="red", fg="yellow", font=("Helvetica", 35, "bold"))
        title_lbl.place(relx=0.5, rely=0.03, width=1540, height=45, anchor=CENTER)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="White")
        main_frame.place(x=20, y=55, width=1480, height=600)

        self.setup_left_frame(main_frame)
        self.setup_right_frame(main_frame)

    def fetch_system_time(self):
        """Automatically updates the variables with system time"""
        now = datetime.now()
        self.var_atten_date.set(now.strftime("%d/%m/%Y"))
        self.var_atten_time.set(now.strftime("%H:%M:%S"))

    def setup_images(self):
        try:
            self.photoimg13 = ImageTk.PhotoImage(Image.open("Image_1/13.jpg").resize((800, 200)))
            Label(self.root, image=self.photoimg13).place(x=0, y=0, width=800, height=200)

            self.photoimg15 = ImageTk.PhotoImage(Image.open("Image_1/15.jpg").resize((800, 200)))
            Label(self.root, image=self.photoimg15).place(x=800, y=0, width=750, height=140)

            self.photoimg4 = ImageTk.PhotoImage(Image.open("Image_1/background.jpg").resize((1550, 900)))
        except Exception as e:
            print(f"Error loading images: {e}")

    def setup_left_frame(self, parent):
        Left_frame = LabelFrame(parent, bd=2, relief=RIDGE, text="Attendance Student Details", font=("Helvetica", 15, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=580)

        try:
            imgStL1 = ImageTk.PhotoImage(Image.open("Image_1/studentattendancedet.webp").resize((820, 150)))
            Label(Left_frame, image=imgStL1).place(x=0, y=0, width=719, height=140)
            self.photoimgStL1 = imgStL1
        except:
            pass

        frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="White")
        frame.place(x=0, y=135, width=720, height=350)

        # Labels and Entries
        labels = [
            ("AttendanceID:", self.var_atten_id),
            ("Roll:", self.var_atten_roll),
            ("Name:", self.var_atten_name),
            ("Department:", self.var_atten_dep),
            ("Time:", self.var_atten_time), # Now using the variable
            ("Date:", self.var_atten_date)  # Now using the variable
        ]

        for i, (text, var) in enumerate(labels):
            Label(frame, text=text, bg="white", font="comicsansns 11 bold").grid(row=i//2, column=(i%2)*2, padx=10, pady=5)
            
            # Make Time and Date Readonly so users can't edit the system time
            state = "readonly" if text in ["Time:", "Date:"] else "normal"
            ttk.Entry(frame, width=22, textvariable=var, font="comicsansns 11 bold", state=state).grid(row=i//2, column=(i%2)*2+1, pady=5)

        Label(frame, text="Attendance Status", bg="white", font="comicsansns 11 bold").grid(row=3, column=0, pady=8)
        self.atten_status = ttk.Combobox(frame, width=20, textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=180, width=710, height=50)

        Button(btn_frame, text="Import csv", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export csv", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="green", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="red", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="indigo", fg="white").grid(row=0, column=3)

    def setup_right_frame(self, parent):
        Right_frame = LabelFrame(parent, bd=2, relief=RIDGE, text="Attendance Details", font=("Helvetica", 15, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=710, height=445)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                  column=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        for col in ("id", "roll", "name", "department", "time", "date", "attendance"):
            self.AttendanceReportTable.heading(col, text=col.capitalize())
            self.AttendanceReportTable.column(col, width=100)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if fln:
            with open(fln, "r") as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Exported", f"Your data exported successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        data = content["values"]
        if data:
            self.var_atten_id.set(data[0])
            self.var_atten_roll.set(data[1])
            self.var_atten_name.set(data[2])
            self.var_atten_dep.set(data[3])
            self.var_atten_time.set(data[4])
            self.var_atten_date.set(data[5])
            self.var_atten_attendance.set(data[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.fetch_system_time() # Reset to current time
        self.var_atten_attendance.set("Status")

    def delete_data(self):
        selected = self.AttendanceReportTable.selection()
        if not selected:
            messagebox.showerror("Error", "No record selected")
            return
        for sel in selected:
            self.AttendanceReportTable.delete(sel)
        self.reset_data()

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()