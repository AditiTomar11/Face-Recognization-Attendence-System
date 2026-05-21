from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os

# Dummy main import placeholder
# from main import Face_Recognition_System

class Face_Recognition_System:
    def __init__(self, root):
        root.title("Main App")
        root.geometry("400x200")
        Label(root, text="Welcome to Face Recognition System", font=("Arial", 16)).pack(pady=40)

class LoginSignup:
    def __init__(self, root):
        self.root = root
        self.root.title("Login & Signup")
        self.root.geometry("800x500+300+150")
        self.root.configure(bg="#1e1e2f")

        # Connect to MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ayodhya2024@",
            database="face_recognizzer"
        )
        self.cursor = self.db.cursor()

        # Load and set background image
        self.bg_img = Image.open("background.jpg") if os.path.exists("background.jpg") else Image.new("RGB", (800, 500), "#1e1e2f")
        self.bg_img = self.bg_img.resize((800, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.main_frame = Frame(self.root, bg="#ffffff", bd=2)
        self.main_frame.place(x=220, y=80, width=360, height=340)

        self.login_ui()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def login_ui(self):
        self.clear_frame()
        Label(self.main_frame, text="Login", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#333").pack(pady=10)

        Label(self.main_frame, text="Username", bg="#ffffff").pack()
        self.login_username = Entry(self.main_frame, font=("Arial", 12))
        self.login_username.pack(pady=5)

        Label(self.main_frame, text="Password", bg="#ffffff").pack()
        self.login_password = Entry(self.main_frame, show="*", font=("Arial", 12))
        self.login_password.pack(pady=5)

        Button(self.main_frame, text="Login", command=self.login_user, bg="#1e90ff", fg="white", font=("Arial", 12, "bold")).pack(pady=15)
        Label(self.main_frame, text="Don't have an account?", bg="#ffffff").pack()
        Button(self.main_frame, text="Go to Signup", command=self.signup_ui, bg="white", fg="#1e90ff", bd=0).pack()

    def signup_ui(self):
        self.clear_frame()
        Label(self.main_frame, text="Signup", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#333").pack(pady=10)

        Label(self.main_frame, text="Full Name", bg="#ffffff").pack()
        self.signup_name = Entry(self.main_frame, font=("Arial", 12))
        self.signup_name.pack(pady=5)

        Label(self.main_frame, text="Email", bg="#ffffff").pack()
        self.signup_email = Entry(self.main_frame, font=("Arial", 12))
        self.signup_email.pack(pady=5)

        Label(self.main_frame, text="Username", bg="#ffffff").pack()
        self.signup_username = Entry(self.main_frame, font=("Arial", 12))
        self.signup_username.pack(pady=5)

        Label(self.main_frame, text="Password", bg="#ffffff").pack()
        self.signup_password = Entry(self.main_frame, show="*", font=("Arial", 12))
        self.signup_password.pack(pady=5)

        Button(self.main_frame, text="Register", command=self.register_user, bg="#28a745", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
        Label(self.main_frame, text="Already have an account?", bg="#ffffff").pack()
        Button(self.main_frame, text="Go to Login", command=self.login_ui, bg="white", fg="#28a745", bd=0).pack()

    def register_user(self):
        name = self.signup_name.get()
        email = self.signup_email.get()
        username = self.signup_username.get()
        password = self.signup_password.get()

        if name == "" or email == "" or username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            self.cursor.execute("INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)",
                                (name, email, username, password))
            self.db.commit()
            messagebox.showinfo("Success", "Signup successful! Please login.")
            self.login_ui()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    def login_user(self):
        username = self.login_username.get()
        password = self.login_password.get()

        self.cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        result = self.cursor.fetchone()

        if result:
            messagebox.showinfo("Login Success", f"Welcome {result[1]}!")
            self.root.destroy()
            main_root = Tk()
            obj = Face_Recognition_System(main_root)
            main_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

if __name__ == "__main__":
    root = Tk()
    app = LoginSignup(root)
    root.mainloop()
