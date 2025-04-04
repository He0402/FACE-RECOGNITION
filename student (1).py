from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox   


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student") 
        # variables
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_dob=StringVar()
        self.var_hostel=StringVar()
        self.var_room=StringVar()
        self.var_pnum=StringVar()
        self.var_phone=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_dep=StringVar()
        self.var_add=StringVar()
        



        #logo
        img = Image.open(r"C:\Users\india\Downloads\JNTU_Hyderabad_logo.png")
        img = img.resize((200,130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-300, y=0, width=800, height=130)

        #2
        img1 = Image.open(r"C:\Users\india\Downloads\lib.jpg")
        img1 = img1.resize((755, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=195, y=0, width=800, height=130)
        #3

        img2 = Image.open(r"C:\Users\india\Downloads\4.jpg")
        img2 = img2.resize((320, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=330, height=130)



        #bg
        img3 = Image.open(r"C:\Users\india\Downloads\back.jpg")
        img3 = img3.resize((1530,720))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1500, height=520)

        #title bloc
        title_lbl=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",35,"bold"),fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=35)
        #main box
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=80,y=100,width=1200,height=600)
        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="current course")
        current_course_frame.place(x=50,y=10,width=1120,height=60)
        #DEPARTMENT
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=20,sticky=W)

        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        dep_combo["values"]=("select deperatment","CSE","ECE","EEE","MECH","CIVIL","CHEMICAL","MET","BBA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=20,pady=10,sticky=W)
        # COURSE
        course_label=Label(current_course_frame,text="select course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=20,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"))
        course_combo["values"]=("select","regular","IDP","IDDMP","PG")
        course_combo.current(0)
        course_combo.grid(row=0,column=4,padx=20,sticky=W)
        #year
        year_label=Label(current_course_frame,text="year",font=("times new roman",12,"bold"))
        year_label.grid(row=0,column=5,padx=20,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"))
        year_combo["values"]=("select","I","II","III","IV","V")
        year_combo.current(0)
        year_combo.grid(row=0,column=6,padx=20,pady=2,sticky=W)

       #student info
        class_Student_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="STUDENT DETAILS")
        class_Student_frame.place(x=50,y=80,width=450,height=260)
        #id
        id_label=Label(class_Student_frame,text="student id :",font=("times new roman",13,"bold")) 
        id_label.grid(row=0,column=0,padx=5,sticky=W)

        ID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_id,text="student id:",font=("times new roman",13,"bold"))
        ID_entry.grid(row=0,column=1,padx=5,sticky=W)
         #name
        name_label=Label(class_Student_frame,text="student name :",font=("times new roman",13,"bold")) 
        name_label.grid(row=1,column=0,padx=5,sticky=W)

        studentNAME_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,text="student name:",font=("times new roman",13,"bold"))
        studentNAME_entry.grid(row=1,column=1,padx=5,sticky=W)
         #dob
        dob_label=Label(class_Student_frame,text="date of birth :",font=("times new roman",13,"bold")) 
        dob_label.grid(row=2,column=0,padx=5,sticky=W)

        DOB_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,text="date of birth:",font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=1,padx=5,sticky=W)
         #hostel
        hostel_label=Label(class_Student_frame,text="hostel name :",font=("times new roman",13,"bold")) 
        hostel_label.grid(row=3,column=0,padx=5,sticky=W)

        HOSTEL_entry=ttk.Entry(class_Student_frame,textvariable=self.var_hostel,text="hostel name:",font=("times new roman",13,"bold"))
        HOSTEL_entry.grid(row=3,column=1,padx=5,sticky=W)
         #room
        room_label=Label(class_Student_frame,text="ROOM NUMBER :",font=("times new roman",13,"bold")) 
        room_label.grid(row=4,column=0,padx=5,sticky=W)

        ROOM_entry=ttk.Entry(class_Student_frame,textvariable=self.var_room,text="ROOM NUMBER:",font=("times new roman",13,"bold"))
        ROOM_entry.grid(row=4,column=1,padx=5,sticky=W)
         #parents
        pnum_label=Label(class_Student_frame,text="PARENTS NUMBER :",font=("times new roman",13,"bold")) 
        pnum_label.grid(row=5,column=0,padx=5,sticky=W)

        PNUM_entry=ttk.Entry(class_Student_frame,textvariable=self.var_pnum,text="PARENT NUMBER:",font=("times new roman",13,"bold"))
        PNUM_entry.grid(row=5,column=1,padx=5,sticky=W)
         #num
        phone_label=Label(class_Student_frame,text="NUMBER :",font=("times new roman",13,"bold")) 
        phone_label.grid(row=6,column=0,padx=5,sticky=W)

        PHONE_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,text="NUMBER:",font=("times new roman",13,"bold"))
        PHONE_entry.grid(row=6,column=1,padx=5,sticky=W)
        #address
        add_label=Label(class_Student_frame,text="ADDRESS:",font=("times new roman",13,"bold")) 
        add_label.grid(row=7,column=0,padx=5,sticky=W)

        PHONE_entry=ttk.Entry(class_Student_frame,textvariable=self.var_add,text="ADRESS:",font=("times new roman",13,"bold"))
        PHONE_entry.grid(row=7,column=1,padx=5,sticky=W)
       


        #bbuttons frame
        

        btn_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="button ")
        btn_frame.place(x=50,y=340,width=300,height=160)
        #sAVE
        img_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("times new roman",13,"bold"),bg="BLUE",fg="white")
    
        img_btn.grid(row=0,column=1)
        #search table
        search_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="search system")
        search_frame.place(x=500,y=70,width=650,height=60)
        #seach
        se_label=Label(search_frame,text="search",font=("times new roman",12,"bold"))
        se_label.grid(row=0,column=0,padx=20,sticky=W)

        #search box
        se_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"))
        se_combo["values"]=("department","branch","year","name","id")

        se_combo.current(0)
        se_combo.grid(row=0,column=1,padx=20,pady=10,sticky=W)
        # search button
        se_btn=Button(search_frame,text="Search",width=13,font=("times new roman",13,"bold"),bg="red",fg="white")
        
        se_btn.grid(row=0,column=2,padx=20,pady=10,sticky=W)
        #SHOW ALL
        se_btn=Button(search_frame,text="SHOW ALL",width=13,font=("times new roman",13,"bold"),bg="red",fg="white")
        
        se_btn.grid(row=0,column=3,padx=20,pady=10,sticky=W)
        #table stdent details
        table_frame=LabelFrame(main_frame,bd=4,bg="pink",relief=RIDGE,text="STUDENT details")
        table_frame.place(x=500,y=136,width=600,height=250)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("id","name","department","year","branch"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("id",text="id")
        self.student_table.heading("name",text="name")
        self.student_table.heading("department",text="department")
        self.student_table.heading("year",text="year")
        self.student_table.heading("branch",text="branch")



        self.student_table.column("department",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("branch",width=100)
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
    
    def add_data(self):
         dep = self.var_dep.get()
         
         if dep=="select department":
             
             messagebox.showerror("error","all fields are required")
            
         else:
            pass
    
   
             

         










        
       
      
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
