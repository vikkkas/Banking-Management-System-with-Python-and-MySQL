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
        
        self.salutation=StringVar()
        self.firstname=StringVar()
        self.lastname=StringVar()
        self.aadhar=StringVar()
        self.pan=StringVar()
        self.id=StringVar()
        self.acc_no=StringVar()
        self.acc_type=StringVar()
        self.acc_bal=StringVar()
        
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
        
        comsalutation=ttk.Combobox(dataframeLeft,textvariable=self.salutation,state="readonly",font=("arial",12,"bold"),
                                   width=33)
        comsalutation["value"]=('--Select--','Mr.','Ms.','Mrs.')
        comsalutation.current(0)
        comsalutation.grid(row=0,column=1)
        
        lblfirst=Label(dataframeLeft, font=("arial",12, "bold"),text="First Name:",padx=2)
        lblfirst.grid(row=1,column=0,sticky=W)
        txtfirst=Entry(dataframeLeft, font=("arial",13, "bold"),textvariable=self.firstname,width=35)
        txtfirst.grid(row=1,column=1)
        
        lblsecond=Label(dataframeLeft, font=("arial",12, "bold"),text= "Second Name: ",padx=2,pady=4)
        lblsecond.grid(row=2,column=0,sticky=W)
        txtsecond=Entry(dataframeLeft, font=("arial",13, "bold"),textvariable=self.lastname,width=35)
        txtsecond.grid(row=2,column=1)
        
        lblaadhar=Label(dataframeLeft,font=("arial",12,"bold"),text="Aadhar No:",padx=2,pady=6)
        lblaadhar.grid(row=3,column=0, sticky=W)
        txtaadhar=Entry(dataframeLeft,font=("arial",13, "bold"),textvariable=self.aadhar,width=35)
        txtaadhar.grid(row=3,column=1)
        
        lblPan=Label(dataframeLeft,font=("arial",12,"bold"),text="Pan No:",padx=2,pady=6)
        lblPan.grid(row=4,column=0, sticky=W)
        txtPan=Entry(dataframeLeft,font=("arial",13, "bold"),textvariable=self.pan,width=35)
        txtPan.grid(row=4,column=1)
        
        lblid=Label(dataframeLeft,font=("arial",12,"bold"),text="Customer Id:",padx=2,pady=6)
        lblid.grid(row=5,column=0, sticky=W)
        txtid=Entry(dataframeLeft,font=("arial",13, "bold"),textvariable=self.id,width=35)
        txtid.grid(row=5,column=1)
        
        lblAcc_No=Label(dataframeLeft,font=("arial",12,"bold"),text="Account No:",padx=2,pady=6)
        lblAcc_No.grid(row=6,column=0, sticky=W)
        txtAcc_No=Entry(dataframeLeft,font=("arial",13, "bold"),textvariable=self.acc_no,width=35)
        txtAcc_No.grid(row=6,column=1)
        
        lblAcc_Type=Label(dataframeLeft,text="Account Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAcc_Type.grid(row=7, column=0)
        
        comAcc_Type=ttk.Combobox(dataframeLeft,textvariable=self.acc_type,state="readonly",font=("arial",12,"bold"),
                                   width=33)
        comAcc_Type["value"]=('--Select--','Savings','Current','Fixed')
        comAcc_Type.current(0)
        comAcc_Type.grid(row=7,column=1)
        
        lblbal=Label(dataframeLeft,font=("arial",12,"bold"),text="Balance",padx=2,pady=6)
        lblbal.grid(row=8,column=0, sticky=W)
        txtbal=Entry(dataframeLeft,textvariable=self.acc_bal,font=("arial",13, "bold"),width=35)
        txtbal.grid(row=8,column=1)
        
        #======================================dataframe right========================================================
        self.txtaccount=Text(dataframeright,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtaccount.grid(row=0,column=0)
        
        #=====================================BUTTONS========================================
        btnaccount=Button(buttonframe,command=self.iaccount_info,text="Account Info",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnaccount.grid(row=0,column=0)
        
        btnrecord_entry=Button(buttonframe,command=self.irecord_entry,text="Submit",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnrecord_entry.grid(row=0,column=1)
        
        btnupdate=Button(buttonframe,command=self.update_data,text="Update",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnupdate.grid(row=0,column=2)
        
        btndelete=Button(buttonframe,command=self.idelete,text="Delete",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btndelete.grid(row=0,column=3)
        
        btnclear=Button(buttonframe,command=self.clear,text="Clear",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnclear.grid(row=0,column=4)
        
        btnexit=Button(buttonframe,command=self.iexit,text="Exit",fg="white",bg="green",font=("arial",12,"bold"),width=23,padx=2,pady=6)
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
        self.bank_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
# ===========================================Functionality Declaration=======================================================================

    def irecord_entry(self):
        if self.aadhar.get()=="" or self.pan.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vikas654321",database="bank_data")
            my_cursor=conn.cursor()
            my_cursor.execute("Insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.salutation.get(),self.firstname.get(),self.lastname.get(),self.aadhar.get(),self.pan.get(),self.id.get(),self.acc_no.get(),self.acc_type.get(),self.acc_bal.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Vikas654321",database="bank_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from bank")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.bank_table.delete(*self.bank_table.get_children())
            for i in rows:
                self.bank_table.insert("",END,values=i)
            conn.commit()
            
        conn.close()
    
    
    def get_cursor(self,event=""):
        cursor_row=self.bank_table.focus()
        content=self.bank_table.item(cursor_row)
        row=content["values"]
        self.salutation.set(row[0])
        self.firstname.set(row[1])
        self.lastname.set(row[2])
        self.aadhar.set(row[3])
        self.pan.set(row[4])
        self.id.set(row[5])
        self.acc_no.set(row[6])
        self.acc_type.set(row[7])
        self.acc_bal.set(row[8])
        
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Vikas654321",database="bank_data")
        my_cursor=conn.cursor()
        sql_command="Update bank SET salutation=%s,first_name=%s,last_name=%s,aadhar=%s,pan=%s,customer_id=%s,acc_no=%s,acc_type=%s,balance=%s where aadhar=%s"
        salutation=self.salutation.get()
        first_name=self.firstname.get()
        last_name=self.lastname.get()
        aadhar=self.aadhar.get()
        pan=self.pan.get()
        customer_id=self.id.get()
        account_no=self.acc_no.get()
        account_type=self.acc_type.get()
        account_balance=self.acc_bal.get()
        inputs=(salutation,first_name,last_name,aadhar,pan,customer_id,account_no,account_type,account_balance,aadhar)

        my_cursor.execute(sql_command,inputs)

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Update","Record has been updated successfully.")

    def iaccount_info(self):
        self.txtaccount.insert(END,"Full Name:\t\t\t"+self.salutation.get()+" "+self.firstname.get()+" ",self.lastname.get()+"\n");
        self.txtaccount.insert(END,"\n\nAadhar No:\t\t\t"+self.aadhar.get()+"\n")
        self.txtaccount.insert(END,"\n PAN No:\t\t\t"+self.pan.get()+"\n")
        self.txtaccount.insert(END,"\nCustomer id:\t\t\t"+self.id.get()+"\n")
        self.txtaccount.insert(END,"\nAccount Number:\t\t\t"+self.acc_no.get()+"\n")
        self.txtaccount.insert(END,"\nAccount Type:\t\t\t"+self.acc_type.get()+"\n")
        self.txtaccount.insert(END,"\nAccount Balance:\t\t\t"+self.acc_bal.get()+"\n")
        
    def idelete(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Vikas654321",database="bank_data")
        my_cursor=conn.cursor()
        query="delete from bank where Aadhar = %s "
        value=(self.aadhar.get(),)
        my_cursor.execute(query,value)        

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Customer Data has been deleted successfully.")
    
    def clear(self):
        self.salutation.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.aadhar.set("")
        self.pan.set("")
        self.id.set("")
        self.acc_no.set("")
        self.acc_type.set("")
        self.acc_bal.set("")
        self.txtaccount.delete("1.0",END)
    
    def iexit(self):
        iexit=messagebox.askyesno("Bank Management System","Confirm you want to exit")
        if iexit>0:
            root.destroy()
            return


root=Tk()
ob=bank(root)
root.mainloop()

