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
import os

import numpy as np



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #title
        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)


        img_top = Image.open(r"college_images\traindata1.jpg")
        img_top = img_top.resize((1367,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1367,height=325)



        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=368,width=1367,height=57)


        img_bottom = Image.open(r"college_images\traindata2.jpg")
        img_bottom = img_bottom.resize((1367,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=425,width=1367,height=325)
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #GRAYSCALE
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            #C:\Users\dSourav\Desktop\Face_recognition_system\data\user.1.9.jpg
            #=========================0===========================|======1=====
                                                                 #|=0=|1|2.....
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        #========================train classifier and save it===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!!")
























if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()