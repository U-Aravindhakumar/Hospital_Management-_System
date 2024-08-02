from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameofTablet=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NoofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.storageAdvice=StringVar()   
        self.DrivingUsingmachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsnumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()



        lbltitle = Label(self.root,bd = 20, relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",
                         font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
 # ========================= Data Freameh ================== #    
        DataFrame= Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=120,width=1360,height=375)  

        DataFrameLeft = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                   font=("times new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=8,width=980,height=330)
        DataFrameRight= LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                   font=("times new roman",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=8,width=330,height=330)

 # ======================== Buttons fream =================== #     
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=490,width=1360,height=70)
       
 # ======================= Details fream ================== #
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=560,width=1360,height=150)
       
 #======================== Dataframe left ================= #

        lblNameTablet = Label(DataFrameLeft,font=("arial",12,"bold"),text="Name of Tablet : ",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet = ttk.Combobox(DataFrameLeft,textvariable=self.NameofTablets,state="readonly",
                                     font=("arial",12,"bold"),width=33)
        comNametablet['value'] = ("nice","Haemophilus influenzae type b", "Hepatitis B.", 
                                  "Human papillomavirus", 
                                  "Whooping cough",
                                  "Meningococcal disease.", "Shingles")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataFrameLeft,font=("arial",12,"bold"),text="Refence No : ",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose : ",padx=2 , pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNooftablets = Label(DataFrameLeft,font=("arial",12,"bold"),text="No of Tablets: ",padx=2, pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNooftablets = Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.NoofTablets,width=35)
        txtNooftablets.grid(row=3,column=1)

        lbllot = Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot ",padx=2, pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtlot.grid(row=4,column=1)

        lblissuedate = Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date : ",padx=2, pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissuedate.grid(row=5,column=1)

        lblexp = Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date : ",padx=2, pady=6)
        lblexp.grid(row=6,column=0,sticky=W)
        txtexp= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtexp.grid(row=6,column=1)

        lbldd = Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose : ",padx=2, pady=4)
        lbldd.grid(row=7,column=0,sticky=W)
        txtdd= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtdd.grid(row=7,column=1)

        lblside = Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect : ",padx=2, pady=4)
        lblside.grid(row=8,column=0,sticky=W)
        txtside= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.sideEfect,width=35)
        txtside.grid(row=8,column=1)

        lblfi = Label(DataFrameLeft,font=("arial",12,"bold"),text="Further information : ",padx=2, pady=4)
        lblfi.grid(row=0,column=2,sticky=W)
        txtfi= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtfi.grid(row=0,column=3)

        lblbp = Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure : ",padx=2, pady=4)
        lblbp.grid(row=1,column=2,sticky=W)
        txtbp= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.DrivingUsingmachine,width=35)
        txtbp.grid(row=1,column=3)

        lblddl = Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice : ",padx=2, pady=4)
        lblddl.grid(row=2,column=2,sticky=W)
        txtddl= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.storageAdvice,width=35)
        txtddl.grid(row=2,column=3)

        lblmed = Label(DataFrameLeft,font=("arial",12,"bold"),text="Madication : ",padx=2, pady=4)
        lblmed.grid(row=3,column=2,sticky=W)
        txtmed= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtmed.grid(row=3,column=3)

        lblpid = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id  ",padx=2, pady=4)
        lblpid.grid(row=4,column=2,sticky=W)
        txtpid= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.PatientId,width=35)
        txtpid.grid(row=4,column=3)

        lblnhs = Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number : ",padx=2, pady=4)
        lblnhs.grid(row=5,column=2,sticky=W)
        txtnhs= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.nhsnumber,width=35)
        txtnhs.grid(row=5,column=3)

        lblpn = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name : ",padx=2, pady=4)
        lblpn.grid(row=6,column=2,sticky=W)
        txtpn= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtpn.grid(row=6,column=3)

        lbldob = Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth : ",padx=2, pady=4)
        lbldob.grid(row=7,column=2,sticky=W)
        txtdob= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtdob.grid(row=7,column=3)

        lblpad = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address : ",padx=2, pady=4)
        lblpad.grid(row=8,column=2,sticky=W)
        txtpad= Entry(DataFrameLeft,font = ("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtpad.grid(row=8,column=3)

 # ====================== Data freame right =========================== #

        self.txtPrescription =Text(DataFrameRight,font = ("arial",13,"bold"),width=32,height=15,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

 

 # ============================== buttons ================================== #

        btnpres = Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",13,"bold"),width=21)
        btnpres.grid(row=0,column=0)

        btnpresdata = Button(Buttonframe,text="Prescription data",bg="green",fg="white",font=("arial",13,"bold"),width=21)
        btnpresdata.grid(row=0,column=1)

        btnupdate = Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",13,"bold"),width=21)
        btnupdate.grid(row=0,column=2)

        btndelete = Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",13,"bold"),width=21)
        btndelete.grid(row=0,column=3)

        btnclear = Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",13,"bold"),width=21)
        btnclear.grid(row=0,column=4)

        btnexit = Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",13,"bold"),width=21)
        btnexit.grid(row=0,column=5)

 # ===================================== table ======================================= #

        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose",
                                                                 "nooftablets", "lot","issuedate","expdate","dailydose",
                                                                 "storage","nhsnumber","pname","dob","address"),
                                                                 xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Referance No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="DailyDose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=3)
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        

 # ======================= funtionality declareation ====================== #

    def iprescriptionData(self):
       if self.NameofTablet.get()=="" or self.ref.get()=="":
           messagebox.showerror("Error","All fields are require")
       else:
           conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
           my_cursor=conn.cursor()
           my_cursor.execute("insert intohospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.NameofTable.get(),
                                                                                                   self.ref.get(),
                                                                                                   self.Dose.get(),
                                                                                                   self.NoofTablets.get(),
                                                                                                   self.Lot.get(),
                                                                                                   self.Issuedate.get(),
                                                                                                   self.ExpDate.get(),
                                                                                                   self.DailyDose.get(),
                                                                                                   self.storageAdvice.get(),
                                                                                                   self.nhsnumber.get(),
                                                                                                   self.PatientName.get(),
                                                                                                   self.DateOfBirth.get(),
                                                                                                   self.PatientAddress.get()
                                                                                                   
                                                                                                   ))
           conn.commit()
           conn.close()































root = Tk()
object=Hospital(root)
root.mainloop()
