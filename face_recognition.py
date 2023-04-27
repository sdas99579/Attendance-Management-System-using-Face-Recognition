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
from time import strftime
from datetime import datetime
import cv2
import os

import numpy as np



class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title
        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=45)


        img_top = Image.open(r"college_images\facerg2.webp")
        img_top = img_top.resize((1367,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1367,height=700)

        b1_1=Button(self.root,text="SCAN FACE",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="red",fg="white")
        b1_1.place(x=580,y=660,width=200,height=45)
        # ========================attendance=============================
    def mark_attendance(self,i,r,n,d):
        with open("sourav.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in  myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H: %M: %S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
    


    #=========================face recognition==========================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))


                conn=mysql.connector.connect(host="localhost",username="root",password="SouravDas@1",database="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                # n=str(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                # r=str(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                # d=str(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                # i=str(i)

                if n == "None" or r == "None" or d == "None":
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                elif confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # self.mark_attendance(i,r,n,d)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            # messagebox.showinfo("Result","completed")




















if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()