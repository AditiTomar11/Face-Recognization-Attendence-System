from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np
import cv2
import os

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="TRAIN DATA SET", bg="green", fg="white", font=("Helvetica", 35, "bold"))
        title_lbl.place(relx=0.5, rely=0.03, width=1540, height=45, anchor=CENTER)

        # Top Image
        try:
            img_top = Image.open("Image_1\StL1.jpg")  # Replace with an actual existing image path
        except:
            img_top = Image.new("RGB", (820, 150), color="gray")
        img_top = img_top.resize((820, 150))
        self.photoimgStL1 = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimgStL1)
        f_lbl1.place(x=0, y=55, width=719, height=140)

        # Train Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",bg="darkred", fg="white", font=("Helvetica", 30, "bold"))
        b1_1.place(x=0, y=380, width=1540, height=45)

        # Bottom Image
        try:
            img_bottom = Image.open("Image_1\background.jpg")  # Replace with an actual existing image path
        except:
            img_bottom = Image.new("RGB", (1530, 325), color="lightgray")
        img_bottom = img_bottom.resize((1530, 325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data folder not found!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
            except:
                continue

        ids = np.array(ids)

        if len(ids) == 0:
            messagebox.showerror("Error", "No valid images found for training!")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
