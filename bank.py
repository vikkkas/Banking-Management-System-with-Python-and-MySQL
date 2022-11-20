from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class bank:
    def __init__(self,root):
        self.root=root
        self.root.title("Bank management system")
        self.root.geometry("1540x800+0+0")
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="BANK MANAGEMENT SYSTEM",fg='red',bg='white',font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
        #===========================DATAFRAME===================================================
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=130,width=1530,height=400)
        
        dataframeLeft=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",12,"bold"),text="Customer Information")
        dataframeLeft.place(x=0,y=5,width=980,height=350)
        
        dataframeright=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",12,"bold"),text="Account Information")
        dataframeright.place(x=990,y=5,width=500,height=350)
        
        #=================BUTTONS=========================================
        buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        buttonframe.place(x=0,y=530,width=1530,height=70)
        
        #===========================DETAILS_FRAME=================================
        
        detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #===========================dataframeLeft============================
        
        lblsalutation=Label(dataframeLeft,text="Salutation:",font=("arial",12,"bold"),padx=2,pady=6)
        lblsalutation.grid(row=0, column=0)
        
        comsalutation=ttk.Combobox(dataframeLeft,state="readonly",font=("arial",12,"bold"),
                                   width=33)
        comsalutation["value"]=('--Select--','Mr.','Ms.','Mrs.')
        comsalutation.current(0)
        comsalutation.grid(row=0,column=1)
        
        lblfirst=Label(dataframeLeft, font=("arial",12, "bold"),text="First Name:",padx=2)
        lblfirst.grid(row=1,column=0,sticky=W)
        txtfirst=Entry(dataframeLeft, font=("arial",13, "bold"),width=35)
        txtfirst.grid(row=1,column=1)
        
        lblsecond=Label(dataframeLeft, font=("arial",12, "bold"),text= "Second Name: ",padx=2,pady=4)
        lblsecond.grid(row=2,column=0,sticky=W)
        txtsecond=Entry(dataframeLeft, font=("arial",13, "bold"),width=35)
        txtsecond.grid(row=2,column=1)
        
        lblaadhar=Label(dataframeLeft,font=("arial",12,"bold"),text="Aadhar No:",padx=2,pady=6)
        lblaadhar.grid(row=3,column=0, sticky=W)
        txtaadhar=Entry(dataframeLeft,font=("arial",13, "bold"),width=35)
        txtaadhar.grid(row=3,column=1)
        
        lblPan=Label(dataframeLeft,font=("arial",12,"bold"),text="Pan No:",padx=2,pady=6)
        lblPan.grid(row=4,column=0, sticky=W)
        txtPan=Entry(dataframeLeft,font=("arial",13, "bold"),width=35)
        txtPan.grid(row=4,column=1)
        
        lblid=Label(dataframeLeft,font=("arial",12,"bold"),text="Customer Id:",padx=2,pady=6)
        lblid.grid(row=5,column=0, sticky=W)
        txtid=Entry(dataframeLeft,font=("arial",13, "bold"),width=35)
        txtid.grid(row=5,column=1)
        
        lblAcc_No=Label(dataframeLeft,font=("arial",12,"bold"),text="Account No:",padx=2,pady=6)
        lblAcc_No.grid(row=6,column=0, sticky=W)
        txtAcc_No=Entry(dataframeLeft,font=("arial",13, "bold"),width=35)
        txtAcc_No.grid(row=6,column=1)
        
        lblAcc_Type=Label(dataframeLeft,text="Account Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAcc_Type.grid(row=7, column=0)
        
        comAcc_Type=ttk.Combobox(dataframeLeft,state="readonly",font=("arial",12,"bold"),
                                   width=33)
        comAcc_Type["value"]=('--Select--','Savings','Current','Fixed')
        comAcc_Type.current(0)
        comAcc_Type.grid(row=7,column=1)
        
        lblage=Label(dataframeLeft,font=("arial",12,"bold"),text="Age",padx=2,pady=6)
        lblage.grid(row=8,column=0, sticky=W)
        txtage=Entry(dataframeLeft,font=("arial",13, "bold"),width=35)
        txtage.grid(row=8,column=1) 
        
        #======================================dataframe right========================================================
        self.txtaccount=Text(dataframeright,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtaccount.grid(row=0,column=0)
        
        #=====================================BUTTONS========================================
        btnaccount=Button(buttonframe,text="Account",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnaccount.grid(row=0,column=0)
        
        btnaccount_type=Button(buttonframe,text="Account Type",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnaccount_type.grid(row=0,column=1)
        
        btnupdate=Button(buttonframe,text="Update",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnupdate.grid(row=0,column=2)
        
        btndelete=Button(buttonframe,text="Delete",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btndelete.grid(row=0,column=3)
        
        btnclear=Button(buttonframe,text="Clear",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnclear.grid(row=0,column=4)
        
        btnexit=Button(buttonframe,text="Exit",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnexit.grid(row=0,column=5)
        
        #===========================================table==========================
        #========================================scroll bar=======================
        scroll_x=ttk.Scrollbar(detailsframe,orient= HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailsframe,orient= VERTICAL)
        self.bank_table=ttk.Treeview(detailsframe,columns=("Salutation","First Name","Last Name","Aadhar No.","Pan No.","Customer id.","Account Number","Account Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.bank_table.xview)
        scroll_y=ttk.Scrollbar(command=self.bank_table.yview)
        
        
        self.bank_table.heading("Salutation",text="Salutation")
        self.bank_table.heading("First Name",text="First Name")
        self.bank_table.heading("Last Name",text="Last Name")
        self.bank_table.heading("Aadhar No.",text="Aadhaar No.")
        self.bank_table.heading("Pan No.",text="Pan No.")
        self.bank_table.heading("Customer id.",text="Customer id.")
        self.bank_table.heading("Account Number",text="Account Number")
        self.bank_table.heading("Account Type",text= "Account Type")
        
        self.bank_table["show"]="headings"

        self.bank_table.column("First Name",width=100)
        self.bank_table.column("Last Name",width=100)
        self.bank_table.column("Salutation",width=100)
        self.bank_table.column("Aadhar No.",width=100)
        self.bank_table.column("Pan No.",width=100)
        self.bank_table.column("Customer id.",width=100)
        self.bank_table.column("Account Type",width=100)
        
        self.bank_table.pack(fill=BOTH,expand=1)
        

        



root=Tk()
ob=bank(root)
root.mainloop()

