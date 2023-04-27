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



class helpdesk:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="HELPDESK",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)


        img_top = Image.open(r"college_images\help1.webp")
        img_top = img_top.resize((1367,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1367,height=720)

        dev_label=Label(f_lbl,text="Email: sdas99579@gmail.com",font=("times new roman",15,"bold"),fg="#2e3168",bg="#6bacdd")
        dev_label.place(x=280,y=440)



if __name__ == "__main__":
    root = Tk()
    obj = helpdesk(root)
    root.mainloop()