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
        Detailsframe.place(x=0,y=560,width=1360,height=100)
       
 #======================== Dataframe left ================= #

        lblNameTablet = Label(DataFrameLeft,font=("arial",12,"bold"),text="Name of Tablet : ",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet = ttk.Combobox(DataFrameLeft,state="readonly",
                                     font=("arial",12,"bold"),width=33)
        comNametablet['value'] = ("nice","Haemophilus influenzae type b", "Hepatitis B.", 
                                  "Human papillomavirus", 
                                  "Whooping cough",
                                  "Meningococcal disease.", "Shingles")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataFrameLeft,font=("arial",12,"bold"),text="Refence No : ",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose : ",padx=2 , pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNooftablets = Label(DataFrameLeft,font=("arial",12,"bold"),text="No of Tablets: ",padx=2, pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNooftablets = Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtNooftablets.grid(row=3,column=1)

        lbllot = Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot ",padx=2, pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtlot.grid(row=4,column=1)

        lblissuedate = Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date : ",padx=2, pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtissuedate.grid(row=5,column=1)

        lblexp = Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date : ",padx=2, pady=6)
        lblexp.grid(row=6,column=0,sticky=W)
        txtexp= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtexp.grid(row=6,column=1)

        lbldd = Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose : ",padx=2, pady=4)
        lbldd.grid(row=7,column=0,sticky=W)
        txtdd= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtdd.grid(row=7,column=1)

        lblside = Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect : ",padx=2, pady=4)
        lblside.grid(row=8,column=0,sticky=W)
        txtside= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtside.grid(row=8,column=1)

        lblfi = Label(DataFrameLeft,font=("arial",12,"bold"),text="Further information : ",padx=2, pady=4)
        lblfi.grid(row=0,column=2,sticky=W)
        txtfi= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtfi.grid(row=0,column=3)

        lblbp = Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure : ",padx=2, pady=4)
        lblbp.grid(row=1,column=2,sticky=W)
        txtbp= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtbp.grid(row=1,column=3)

        lblddl = Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice : ",padx=2, pady=4)
        lblddl.grid(row=2,column=2,sticky=W)
        txtddl= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtddl.grid(row=2,column=3)

        lblmed = Label(DataFrameLeft,font=("arial",12,"bold"),text="Madication : ",padx=2, pady=4)
        lblmed.grid(row=3,column=2,sticky=W)
        txtmed= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtmed.grid(row=3,column=3)

        lblpid = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id  ",padx=2, pady=4)
        lblpid.grid(row=4,column=2,sticky=W)
        txtpid= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtpid.grid(row=4,column=3)

        lblnhs = Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number : ",padx=2, pady=4)
        lblnhs.grid(row=5,column=2,sticky=W)
        txtnhs= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtnhs.grid(row=5,column=3)

        lblpn = Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name : ",padx=2, pady=4)
        lblpn.grid(row=6,column=2,sticky=W)
        txtpn= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtpn.grid(row=6,column=3)

        lbldob = Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth : ",padx=2, pady=4)
        lbldob.grid(row=7,column=2,sticky=W)
        txtdob= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtdob.grid(row=7,column=3)

        lblpad = Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number : ",padx=2, pady=4)
        lblpad.grid(row=8,column=2,sticky=W)
        txtpad= Entry(DataFrameLeft,font = ("arial",13,"bold"),width=35)
        txtpad.grid(row=8,column=3)







root = Tk()
object=Hospital(root)
root.mainloop()
