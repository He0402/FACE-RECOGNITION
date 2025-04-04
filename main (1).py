import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2
import os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

def assure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

def contact():
    mess.showinfo(title='Contact us', message="Please contact us at: 'xxxxxxxxxxxxx@gmail.com'")

def check_haarcascadefile():
    if not os.path.isfile("haarcascade_frontalface_default.xml"):
        mess.showerror(title='File Missing', message='Please contact us for help')
        window.destroy()

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    key_file = "TrainingImageLabel.txt"
    
    if os.path.isfile(key_file):
        with open(key_file, "r") as tf:
            key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('No Password', 'Please enter a new password', show='*')
        if new_pas is None:
            mess.showerror(title='No Password Entered', message='Password not set! Please try again.')
        else:
            with open(key_file, "w") as tf:
                tf.write(new_pas)
            mess.showinfo(title='Password Registered', message='New password registered successfully!')
        return
    
    op = old.get()
    newp = new.get()
    nnewp = nnew.get()
    
    if op == key:
        if newp == nnewp:
            with open(key_file, "w") as tf:
                tf.write(newp)
            mess.showinfo(title='Password Updated', message='Password updated successfully!')
        else:
            mess.showerror(title='Error', message='New password and confirm password do not match!')
    else:
        mess.showerror(title='Wrong Password', message='The old password is incorrect.')

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")

    tk.Label(master, text='Enter Old Password', bg='white', font=('times', 12, 'bold')).place(x=10, y=10)
    global old
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, 'bold'), show='*')
    old.place(x=180, y=10)
    tk.Label(master, text='Enter New Password', bg='white', font=('times', 12, 'bold')).place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, 'bold'), show='*')
    new.place(x=180, y=45)
    tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, 'bold')).place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, 'bold'), show='*')
    nnew.place(x=180, y=80)
    tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
              activebackground="white", font=('times', 10, 'bold')).place(x=200, y=120)
    tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25,
              activebackground="white", font=('times', 10, 'bold')).place(x=10, y=120)
    master.mainloop()

def psw():
    assure_path_exists("TrainingImageLabel/")
    key_file = "TrainingImageLabel.txt"
    
    if os.path.isfile(key_file):
        with open(key_file, "r") as tf:
            key = tf.read()
    else:
        new_pas = tsd.askstring('No Password', 'Please enter a new password', show='*')
        if new_pas is None:
            mess.showerror(title='No Password Entered', message='Password not set! Please try again.')
        else:
            with open(key_file, "w") as tf:
                tf.write(new_pas)
            mess.showinfo(title='Password Registered', message='New password registered successfully!')
        return
    
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if password == key:
        TakeImages()
    elif password is None:
        pass
    else:
        mess.showerror(title='Wrong Password', message='You have entered the wrong password.')

def clear():
    txt.delete(0, 'end')
    res = "1) Take Images  >>>  2) Save Profile"
    message1.configure(text=res)

def clear2():
    txt2.delete(0, 'end')
    res = "1) Take Images  >>>  2) Save Profile"
    message1.configure(text=res)

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    
    serial = 0
    if os.path.isfile("StudentDetails.csv"):
        with open("StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for _ in reader1:
                serial += 1
        serial = (serial // 2) + 1
    else:
        with open("StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
    
    Id = txt.get()
    name = txt2.get()
    
    if name.isalpha() or ' ' in name:
        cam = cv2.VideoCapture(0)
        haarcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(haarcascadePath)
        sampleNum = 0
        
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum += 1
                cv2.imwrite(f"TrainingImage/{name}.{serial}.{Id}.{sampleNum}.jpg", gray[y:y + h, x:x + w])
                cv2.imshow('Taking Images', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 100:
                break
        
        cam.release()
        cv2.destroyAllWindows()
        
        res = f"Images Taken for ID : {Id}"
        row = [serial, '', Id, '', name]
        
        with open('StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        
        message1.configure(text=res)
    else:
        message1.configure(text="Enter a valid name")

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    haarcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(haarcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    
    if not faces:
        mess.showerror(title='No Registrations', message='Please register someone first!')
        return
    
    recognizer.train(faces, np.array(ID))
    recognizer.save("TrainingImageLabel.yml")
    
    res = "Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text=f'Total Registrations till now: {ID[0]}')

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
    
    return faces, Ids

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    
    for k in tv.get_children():
        tv.delete(k)
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    if os.path.isfile("TrainingImageLabel.yml"):
        recognizer.read("TrainingImageLabel.yml")
    else:
        mess.showerror(title='Data Missing', message='Please click on Save Profile to reset data!')
        return
    
    haarcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(haarcascadePath)
    df = pd.read_csv("StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if conf < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['ID'] == Id]['NAME'].values
                tt = str(Id) + "-" + str(aa[0])
                attendance = [str(Id), '', str(aa[0]), '', date, '', timeStamp]
                tv.insert('', 0, text=Id, values=(str(Id), str(aa[0]), str(date), str(timeStamp)))
            else:
                Id = 'Unknown'
                tt = str(Id)
            
            if conf > 75:
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite(f"ImagesUnknown/Image{noOfFile}.jpg", im[y:y + h, x:x + w])
            
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        
        cv2.imshow('Taking Attendance', im)
        if cv2.waitKey(1) == ord('q'):
            break
    
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    cam.release()
    cv2.destroyAllWindows()
    
    if df is not None:
        with open(f"Attendance/Attendance_{date}_{timeStamp}.csv", 'w+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(col_names)
            writer.writerows([attendance])
        
        message2.configure(text=attendance)

window = tk.Tk()
window.geometry("1280x720")
window.resizable(False, False)
window.title("Face Recognition Attendance System")
window.configure(background='#1B1B1B')

# Widgets and Layout
clock = tk.Label(window, fg="white", bg="#1B1B1B", font=('times', 14, 'bold'))
clock.place(x=1150, y=0)
tick()

# Add your widgets setup below
# Example:
# tk.Label(window, text="Enter ID:", bg='#1B1B1B', fg='white').place(x=50, y=50)
# txt = tk.Entry(window, width=20)
# txt.place(x=150, y=50)
# tk.Button(window, text="Save Profile", command=psw).place(x=50, y=100)

window.mainloop()
import cv2
print(cv2.__version__)
import cv2

# Check if cv2.face module is available
try:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("LBPHFaceRecognizer is available.")
except AttributeError:
    print("cv2.face module or LBPHFaceRecognizer_create() is not available.")
