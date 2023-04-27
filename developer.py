#python interface to the tcl/tk GUI toolkit
from cProfile import label
from logging import root
from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import ttk
#pyhton imaging library (Fork)
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)


        img_top = Image.open(r"college_images\developer.jpg")
        img_top = img_top.resize((1367,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1367,height=720)

        mainframe=Frame(f_lbl,bd=2,bg="#81d5fa")
        mainframe.place(x=1100,y=0,width=370,height=580)

        img_frame = Image.open(r"college_images\sdas.jpeg")
        img_frame = img_frame.resize((250,250),Image.ANTIALIAS)
        self.photoimg_frame=ImageTk.PhotoImage(img_frame)

        f_lbl = Label(mainframe,image=self.photoimg_frame)
        f_lbl.place(x=0,y=0,width=250,height=250)

        dev_label=Label(mainframe,text="Name: Sourav Das",font=("times new roman",15,"bold"),fg="#275477",bg="#81d5fa")
        dev_label.place(x=0,y=260)
        dev_label=Label(mainframe,text="Domain: Software Developer",font=("times new roman",15,"bold"),fg="#275477",bg="#81d5fa")
        dev_label.place(x=0,y=290)
        dev_label=Label(mainframe,text="STD: MCA 6th sem",font=("times new roman",15,"bold"),fg="#275477",bg="#81d5fa")
        dev_label.place(x=0,y=320)
        dev_label=Label(mainframe,text="college: NIT Calicut",font=("times new roman",15,"bold"),fg="#275477",bg="#81d5fa")
        dev_label.place(x=0,y=350)
        dev_label=Label(mainframe,text="Roll No: M200722CA",font=("times new roman",15,"bold"),fg="#275477",bg="#81d5fa")
        dev_label.place(x=0,y=380)
        dev_label=Label(mainframe,text="Batch: 2020-23",font=("times new roman",15,"bold"),fg="#275477",bg="#81d5fa")
        dev_label.place(x=0,y=410)
        dev_label=Label(mainframe,text="Email: sdas99579@gmail.com",font=("times new roman",15,"bold"),fg="#275477",bg="#81d5fa")
        dev_label.place(x=0,y=440)

        









if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()