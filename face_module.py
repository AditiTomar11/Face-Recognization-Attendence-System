from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # === Title Label ===
        title_lbl = Label(self.root, text="FACE RECOGNITION", bg="green", fg="white", font=("Helvetica", 35, "bold"))
        title_lbl.pack(pady=10)

        # === Frame for Side-by-Side Images ===
        image_frame = Frame(self.root, height=720)
        image_frame.pack(pady=10, fill=X)  # Fill horizontally only, no vertical expand

        # === Canvas for Image Overlay ===
        canvas = Canvas(self.root, width=1530, height=700)
        canvas.pack()

        # === Left Image ===
        try:
            img_left = Image.open("Image_1/Stl2.png").resize((765, 700))
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            lbl_left = Label(image_frame, image=self.photoimg_left)
            lbl_left.pack(side=LEFT, padx=5, pady=5)
        except:
            print("Left image not found")

        # === Right Image ===
        try:
            img_right = Image.open("Image_1/1.jpg").resize((765, 700))
            self.photoimg_right = ImageTk.PhotoImage(img_right)
            lbl_right = Label(image_frame, image=self.photoimg_right)
            lbl_right.pack(side=LEFT, padx=5, pady=5)
        except:
            print("Right image not found")


         # === Recognize Button on Top of Image (Centered) ===
        self.b1_1 = Button(self.root, text="FACE RECOGNIZE", command=self.face_recog, cursor="hand2",
                           bg="darkred", fg="white", font=("Helvetica", 30, "bold"))

        # Place button at center bottom of image area (canvas)
        self.b1_1.place(x=950, y=680)  # Adjust as needed

    # === Mark Attendance ===
    def mark_attendance(self, s, i, r, d):
        with open("mayank.csv", "a+", newline="\n") as f:
            f.seek(0)
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]
            if s not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt_string = now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{i},{r},{d},{dt_string},{d1},Present")

    # === Face Recognition Function ===
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="Ayodhya2024@", database="face_recognizzer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Name FROM student WHERE studentid=%s", (id,))
                i = "+".join(my_cursor.fetchone())
                my_cursor.execute("SELECT Roll FROM student WHERE std_id=%s", (id,))
                r = "+".join(my_cursor.fetchone())
                my_cursor.execute("SELECT Dep FROM student WHERE std_id=%s", (id,))
                d = "+".join(my_cursor.fetchone())
                my_cursor.execute("SELECT StudentID FROM student WHERE std_id=%s", (id,))
                s = "+".join(my_cursor.fetchone())

                if confidence > 77:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(img, f"ID:{s}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Dep:{d}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                    self.mark_attendance(s, i, r, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
            return img

        # faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # clf = cv2.face.LBPHFaceRecognizer_create()
        # clf.read("classifier.yml")

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        # === Ensure classifier file exists ===
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Trained model 'classifier.xml' not found!")
            return

        clf.read("classifier.xml")


        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter key to stop
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
