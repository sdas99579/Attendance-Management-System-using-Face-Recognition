#python interface to the tcl/tk GUI toolkit
from logging import root
from tkinter import*
from tkinter import ttk
import tkinter
#pyhton imaging library (Fork)
from PIL import Image,ImageTk

#date time
from time import strftime
from datetime import datetime

from student import Student
from train import Train
from face_recognition import Face_Recognition
import os
from attendance import Attendance
from developer import Developer
from help import helpdesk


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img = Image.open(r"college_images\NITC.webp")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1 = Image.open(r"college_images\second.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=400,height=130)

        #third image
        img2 = Image.open(r"college_images\NITC3.webp")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=500,height=130)

        #bgimg
        img3 = Image.open(r"college_images\bgimg.webp")
        img3 = img3.resize((1370,630),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1370,height=630)

        #title
        title_lbl = Label(bg_img,text="ATTENDANCE USING FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)

        # ==================time==============
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=5,y=0,width=100,height=50)
        time()

        #student button
        img4 = Image.open(r"college_images\student.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details", command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=270,width=220,height=40)

        #face detector button
        img5 = Image.open(r"college_images\fd.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector", cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=270,width=220,height=40)

        #attendance button
        img6 = Image.open(r"college_images\attendance.webp")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=270,width=220,height=40)

        #help button
        img7 = Image.open(r"college_images\help.png")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=270,width=220,height=40)







        #Train data button
        img8 = Image.open(r"college_images\train.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=340,width=220,height=220)

        b1_1=Button(bg_img,text="Train data", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=540,width=220,height=40)

        #photos button
        img9 = Image.open(r"college_images\photo.webp")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=340,width=220,height=220)

        b1_1=Button(bg_img,text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=540,width=220,height=40)

        #Developer button
        img10 = Image.open(r"college_images\dev.jpg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=340,width=220,height=220)

        b1_1=Button(bg_img,text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=540,width=220,height=40)

        #Exit button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=340,width=220,height=220)

        b1_1=Button(bg_img,text="Exit", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=540,width=220,height=40)

#====================photos=================
    def open_img(self):
        os.startfile("data")


        #===============================Function==========================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=helpdesk(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


