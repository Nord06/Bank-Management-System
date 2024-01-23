import random
import os

from tkinter import *
from tkinter import ttk,messagebox as tkMessageBox

root=Tk()
root.geometry("500x450")
root.title("Banking S/W")
root.iconbitmap("hi.ico")

from sqlite3 import *
db=connect("bankdb.db")
d=db.cursor()
    
def clos():
    global cl
    if(cl==1):
        roott8cp()
    elif(cl==2):
        roott4tran()
        

def inp():
    global s,s1,s2
    global name,phone,acc,pas,amt,root
    phone=s1.get()
    acc=random.randint(1000,10000)
    Label(root,text="Account Number Generated for You {}".format(acc),fg="red",bg="Light blue",font=("Arial Rounded MT Bold",12),height=2).place(x=100,y=240)
    db=connect("bankdb.db")
    d=db.cursor()
    d.execute("create table if not exists 'bank'(nam TEXT,phone int,account int,password int,balance int,rm int)")
    d.execute("insert into bank values('{}',{},{},{},1000,0)".format(s.get(),s1.get(),acc,s2.get()))
    db.commit()

def value():
    global s,s1,s2,root
    n=0
    m=0
    o=0
    val=s.get()
    a=s1.get()
    b=s2.get()
    a1=str(a)
    b2=str(b)
    c=len(a1)
    d=len(b2)
    if(s.get()==""):
        Label(root,text="Name*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    else:
        o=1
        Label(root,text="Name",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    if(c==10):
        Label(root,text="Phone",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=130)
        n=1
    else:
        Label(root,text="Phone*(10 digit)",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=190,y=130)
    if(d==4):
        Label(root,text="Password",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=180)
        m=1
    else:
        Label(root,text="Password*(4 digit)",fg="red",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=184,y=180)
    if(n==1 and m==1 and o==1):
        inp()

def check():
    global pa,ac,acc,amt,root
    rec=0
    d.execute("select account from bank where account={}".format(ac.get()))
    db.commit()
    r=d.fetchall()
    if not r:
            Label(root,text="Account Number Not Present",fg="red",bg="Light blue",font=("Arial Rounded MT Bold",12),width=30).place(x=120,y=350)
    else:
        d.execute("select * from bank where account={}".format(ac.get()))
        db.commit()
        rec=d.fetchall()
        for row in rec:
                amt=row[4]
                if(row[3]==pa.get() and row[2]==ac.get()):
                    tran()
                else:
                    Label(root,text="Wrong Password!!!!",fg="red",bg="Light blue",font=("Arial Rounded MT Bold",12),width=30).place(x=100,y=350)

def ck_user():
    global amt,k

    d.execute("select * from bank")
    db.commit()
    r=d.fetchall()
    
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    
    tree = ttk.Treeview(canvas,columns=("1","2","3"),selectmode="browse")
    tree.heading('#0', text="Name",anchor=W)
    tree.heading('1', text="Phone",anchor=W)
    tree.heading('2', text="Account",anchor=W)
    tree.heading('3', text="Balance",anchor=W)
    tree.column("#0", width=110,stretch=NO)
    tree.column("1", width=110, stretch=NO)
    tree.column("2", width=110,stretch=NO)
    tree.column("3", width=110,stretch=NO)

    scrollbar_vertical = ttk.Scrollbar(canvas, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_vertical.set)

    tree.place(x=20,y=20)
    
    scrollbar_vertical.place(x=465, y=20,relheight=0.51)

    print(r)
    len(r)
    for i in range(len(r)):
                tree.insert('','end',text=r[i][0], values=(r[i][1],r[i][2],r[i][4]))
                
    Button(root,text="Back",command=ad_page,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=280)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=320)

def ck_user_rq():
    global amt,k,tree

    d.execute("select * from bank")
    db.commit()
    r=d.fetchall()
    
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    
    tree = ttk.Treeview(canvas,columns=("1","2","3"),selectmode="browse")
    tree.heading('#0', text="Name",anchor=W)
    tree.heading('1', text="Phone",anchor=W)
    tree.heading('2', text="Account",anchor=W)
    tree.heading('3', text="Balance",anchor=W)
    tree.column("#0", width=110,stretch=NO)
    tree.column("1", width=110, stretch=NO)
    tree.column("2", width=110,stretch=NO)
    tree.column("3", width=110,stretch=NO)

    scrollbar_vertical = ttk.Scrollbar(canvas, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_vertical.set)

    tree.place(x=20,y=20)
    
    scrollbar_vertical.place(x=465, y=20,relheight=0.51)

    print(r)
    for i in range(len(r)):
        if(r[i][5]==1):
            tree.insert('','end',text=r[i][0], values=(r[i][1],r[i][2],r[i][4]))
    
    Button(root,text="Accept",command=dele,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=10).place(x=165,y=280)
    Button(root,text="Decline",command=ck_user_rq,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=10).place(x=265,y=280)
              
    Button(root,text="Back",command=ad_page,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=330)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=380)

    
def ad_page():
    global c4,k
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="ADMIN PAGE",fg="navy",bg="Light blue",font=("Cooper Black" ,20)).place(x=170,y=20)
    Button(root,text="Check Accounts",command=ck_user,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=100)
    Button(root,text="Check Users Request",command=ck_user_rq,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=150)
    Button(root,text="Back",command=home,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=250)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=300)

def test():
    global pa,ac,root
    n=0
    m=0
    a=pa.get()
    b=ac.get()
    a1=str(a)
    b2=str(b)
    c=len(a1)
    d=len(b2)
    if(c==4):
            n=1
            Label(root,text="Please Enter Password",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=170,y=130)
    else:
             Label(root,text="Please Enter Password*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=167,y=130)
    if(d==4):
                m=1
                Label(root,text="Please Enter Account Number",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=25).place(x=145,y=80)
    else:
            Label(root,text="Please Enter Account Number*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=142,y=80)
    if(n==1 and m==1):
            check()

def ad_test():
    global ad_pa,ad_ac,root
    if("admin"==str(ad_ac.get()) or "ADMIN"==str(ad_ac.get()) or "Admin"==str(ad_ac.get())):
        if("12345"==str(ad_pa.get())):
            ad_page()

def dele():
    global pa,ac,acc,amt,tree
    db=connect("bankdb.db")
    d=db.cursor()
    
    selected = tree.selection()
    a1=tree.item(selected)['values']
    print("1",a1)
        
    d.execute("delete from bank where account={} ".format(a1[1]))
    db.commit()
    ck_user_rq()
 
def up():
    global pa,ac,acc,amt
    db=connect("bankdb.db")
    d=db.cursor()
    d.execute("update bank set balance={} where account={} ".format(amt,ac.get()))
    db.commit()

def cpup():
    global ac,c4,c3
    a=str(c4.get())
    if(len(a)==4):
        db=connect("bankdb.db")
        d=db.cursor()
        if(cl==2):
            d.execute("update bank set password={} where account={} ".format(c4.get(),ac.get()))
        elif(cl==1):
            d.execute("update bank set password={} where account={} ".format(c4.get(),c3.get()))
        db.commit()
        k=4
        home()
    else:
        Label(root,text="Password*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=10)
def cpin():
    global c4,k
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="Password",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=10)
    c4=IntVar()
    Entry(root,textvariable=c4,bg="white",fg="orangered4",width=20,show="*").place(x=190,y=50)
    Button(root,text="SUMBIT",command=cpup,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=100)

def why():
    global root,k
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="QUERY PAGE",fg="white",bg="Light blue",font=("Cooper Black" ,20)).place(x=120,y=20)
    Label(root,text="LAXMI CHIT FUNDBANK",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=500)
    Label(root,text="1.May You Entered Name Can Be Wrong",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=100)
    Label(root,text="2.May You Entered Phone Number Can Be Wrong",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=150)
    Label(root,text="3.May You Entered Account Number Can Be Wrong",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=200)
    Button(root,text="HOME",command=home,activebackground="red",activeforeground="black",fg="cyan",bg="darkblue",width=20).place(x=180,y=250)

def chpass():
    global c1,c2,c3,root
    db=connect("bankdb.db")
    d=db.cursor()
    d.execute("select account from bank where account={}".format(c3.get()))
    p=d.fetchall()
    if not p:
            Label(root,text="Account Number Not Present*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12),width=30).place(x=120,y=350)
    else:
        d.execute("select * from bank where account={}".format(c3.get()))
        rec=d.fetchall()
        for row in rec:
            if(row[0]==c1.get() and row[1]==c2.get() and row[2]==c3.get()):
                  cpin()
            else:
                Button(root,text="Why Can Not Change Password?",command=why,activebackground="red",activeforeground="black",fg="skyblue",bg="darkblue",width=40).place(x=120,y=350)
                Label(root,text="Can Not Change Password",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=30,height=3).place(x=110,y=240)
                 
def change():
    global c1,c2,c3,root
    a=str(c3.get())
    b=str(c2.get())
    n=0
    m=0
    o=0
    if(c1.get()==""):
         Label(root,text="Name*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    else:
        o=1
        Label(root,text="Name",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=80)
    if(len(a)==4):
        n=1
        Label(root,text="Account Number",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=180)
    else:
        Label(root,text="Account Number*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=180)
    if(len(b)==10):
        m=1
        Label(root,text="Phone",fg="white",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=130)
    else:
        Label(root,text="Phone*",fg="red2",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=150,y=130)
    if(n==1 and m==1 and o==1):
        chpass()
        
def cp():
    global root,c1,c2,c3,k,cl
    cl=1
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="PASSWORD CHANGING PAGE",fg="navy",bg="Light blue",font=("Cooper Black" ,20)).place(x=45,y=10)
    Label(root,text="Name",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=230,y=80)
    c1=StringVar()
    Entry(root,textvariable=c1,bg="white",fg="orangered4").place(x=195,y=105)
    c1.get()
    Label(root,text="Phone",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=225,y=130)
    c2=IntVar()
    Entry(root,textvariable=c2,bg="white",fg="orangered4").place(x=195,y=155)
    c2.get()
    Label(root,text="Account Number",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=188,y=180)
    c3=IntVar()
    Entry(root,textvariable=c3,bg="white",fg="orangered4").place(x=195,y=205)
    c3.get()
    Button(root,text="SUMBIT",command=change,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=250)
    Button(root,text="HOME",command=home,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=300)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=400)
        
def create():
    global name,phone,acc,pas
    global s,s1,s2,roo,k
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="ACCOUNT CREATING PAGE",fg="Navy",bg="Light blue",font=("Cooper Black" ,20)).place(x=60,y=10)
    acc=random.randint(1000,10000)
    Label(root,text="Hi Customer Follow the Steps to Create Account",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=80,y=50)
    Label(root,text="Name",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=230,y=80)
    s=StringVar()
    Entry(root,textvariable=s,bg="white",fg="orangered4").place(x=195,y=105)
    name=s.get()
    Label(root,text="Phone",fg="BLack",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=225,y=130)
    s1=IntVar()
    Entry(root,textvariable=s1,bg="white",fg="orangered4").place(x=195,y=155)
    Label(root,text="Password",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=210,y=180)
    s2=IntVar()
    Entry(root,textvariable=s2,show="*",bg="white",fg="orangered4").place(x=195,y=205)
    pas=s2.get()
    Button(root,text="SUBMIT",command=value,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=240)
    Button(root,text="HOME",command=home,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=280)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=350)

def login():
    global pa,ac,root,k,cl,rq_var
    rq_var=0
    cl=2
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="LOGIN PAGE",fg="navy",bg="Light blue",font=("Cooper Black" ,20)).place(x=180,y=20)
    Label(root,text="Pease Enter Account Number",fg="BLack",bg="Light blue",font=("Arial Rounded MT Bold",12),width=25).place(x=145,y=80)
    ac=IntVar()
    Entry(root,textvariable=ac,bg="white",fg="orangered4").place(x=195,y=105)
    ac.get()
    Label(root,text="Please Enter Password",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=170,y=130)
    pa=IntVar()
    Entry(root,bg="white",fg="orangered4",textvariable=pa,show="*").place(x=195,y=155)
    pa.get()
    Button(root,text="SUBMIT",command=test,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=200)
    Button(root,text="HOME",command=home,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=240)
    Button(root,text="REQUEST TO DELETE ACC.",command=delt,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=280)
    Button(root,text="FORGET PASSWORD",command=cp,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=320)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=370)

def ad_login():
    global ad_pa,ad_ac,root,k,cl,rq_var
    rq_var=0
    cl=2
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="LOGIN PAGE",fg="Navy",bg="Light blue",font=("Cooper Black" ,20)).place(x=180,y=20)
    Label(root,text="Pease Enter Account Number",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12),width=25).place(x=145,y=80)
    ad_ac=StringVar()
    Entry(root,textvariable=ad_ac,bg="white",fg="orangered4").place(x=195,y=105)
    ad_ac.get()
    Label(root,text="Please Enter Password",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=170,y=130)
    ad_pa=IntVar()
    Entry(root,bg="white",fg="orangered4",textvariable=ad_pa,show="*").place(x=195,y=155)
    ad_pa.get()
    Button(root,text="SUBMIT",command=ad_test,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=200)
    Button(root,text="HOME",command=home,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=240)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=370)
    
def bal():
    global ac,amt,k,root
    
    print (amt)
    d.execute("select * from bank where account={}".format(ac.get()))
    db.commit()
    r=d.fetchall()
    
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    
    tree = ttk.Treeview(canvas,columns=("1","2","3"),selectmode="browse")
    tree.heading('#0', text="Name",anchor=W)
    tree.heading('1', text="Phone",anchor=W)
    tree.heading('2', text="Account",anchor=W)
    tree.heading('3', text="Balance",anchor=W)
    tree.column("#0", width=110,stretch=NO)
    tree.column("1", width=110, stretch=NO)
    tree.column("2", width=110,stretch=NO)
    tree.column("3", width=110,stretch=NO)

    scrollbar_vertical = ttk.Scrollbar(canvas, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_vertical.set)

    tree.place(x=20,y=20)
    
    scrollbar_vertical.place(x=465, y=20,relheight=0.51)
    print(r)
    for i in range(len(r)):
        tree.insert('','end',text=r[i][0], values=(r[i][1],r[i][2],r[i][4]))

    Button(root,text="Back",command=tran,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=280)
    
def wit2():
    global wth,amt,root
    if(100<=wth.get()<=10000):
        if(wth.get()<=amt):
            amt=amt-wth.get()
            up()
            Label(root,text="Your Balance is {}".format(amt),fg="red2",bg="Light blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
        else:
            Label(root,text="Your Balance is Low*",fg="red2",bg="Light blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
    else:
         Label(root,text="Limit Max:₹10000 and Min:₹100*",fg="red2",bg="Light blue",width=20,wraplength=200,font=("Arial Rounded MT Bold",12)).place(x=150,y=260)
         
def add():
    global wth,amt,root
    if(100<=wth.get()<=100000):
        amt=amt+wth.get()
        up()
        Label(root,text="Your Balance is {}".format(amt),fg="white",bg="Light blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
    else:
         Label(root,text="Limit Max:₹100000 and Min:₹100*",fg="red2",bg="Light blue",width=20,wraplength=200,font=("Arial Rounded MT Bold",12)).place(x=152,y=260)
         
def amin():
    global wth,amt,root,k
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="WITHDRAW\DEPOSIT PAGE",fg="navy",bg="Light blue",font=("Cooper Black" ,20)).place(x=50,y=20)
    Label(root,text="Enter Amount :",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=196,y=80)
    wth=IntVar()
    Entry(root,textvariable=wth,bg="white",fg="orangered4").place(x=195,y=105)
    wth.get()
    Button(root,text="Withdraw",command=wit2,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=140)
    Button(root,text="Deposit",command=add,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=180)
    Button(root,text="Back",command=tran,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=220)
    #Label(root,text="Your Balance is {}".format(amt),fg="white",bg="Light blue",width=20,height=2,font=("Arial Rounded MT Bold",12)).place(x=165,y=260)
    Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=300)
    
def tran():
            global amt,root,k
            canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
            canvas.place(x=0,y=0)
            Label(root,text="TRANSCATION  PAGE",fg="navy",bg="Light blue",font=("Cooper BLack" ,20)).place(x=120,y=20)
            Button(root,text="Check Balance",command=bal,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=100)
            Button(root,text="Withdraw/Deposit",command=amin,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=150)
            Button(root,text="Change Password",command=cpin,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=200)
            Button(root,text="Back",command=home,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=250)
            Label(root,text="LAXMI CHIT FUND BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=300)
def delt():
    global pa,ac,r,acc
    print(1)
    n_rq=0
    m_rq=0
    a=pa.get()
    b=ac.get()
    a1=str(a)
    b2=str(b)
    c=len(a1)
    dh=len(b2)
    if(c==4):
            n_rq=1
            Label(root,text="Please Enter Password",fg="black",bg="Light blue",font=("Arial Rounded MT Bold",12),width=20).place(x=170,y=130)
    else:
             Label(root,text="Please Enter Password*",fg="black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=167,y=130)
    if(dh==4):
                m_rq=1
                Label(root,text="Pease Enter Account Number",fg="black",bg="Light blue",font=("Arial Rounded MT Bold",12),width=25).place(x=145,y=80)
    else:
            Label(root,text="Pease Enter Account Number*",fg="black",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=142,y=80)
    if(n_rq==1 and m_rq==1):
        print(2)

        d.execute("select account from bank where account={}".format(ac.get()))
        db.commit()
        r=d.fetchall()
        if not r:
            Label(root,text="Account Number Not Present",fg="red",bg="Light blue",font=("Arial Rounded MT Bold",12),width=30).place(x=120,y=350)
        else:
            d.execute("update bank set rm=1 where account={}".format(ac.get()))
            db.commit()
            tkMessageBox.showinfo("Banking System", "Requested ; It may take time to accept your request")

def take():
    global t1
    if(t1.get()==1):
        create()
    else:
        home()
        
def term():
    global t1,k,root 
    canvas = Canvas(root, width=500, height=550, bd=0, highlightthickness=0, highlightbackground="yellow", bg="Light blue")
    canvas.place(x=0,y=0)
    Label(root,text="Terms and Conditions",fg="navy",bg="Light blue",font=("Cooper Black" ,20)).place(x=120,y=20)
    Label(root,text="LAXMI CHIT FUND  BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=500)
    Label(root,text="1.You Should Credit Account with ₹1000",fg="black",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=100)
    Label(root,text="2.You Can WithDraw Max:₹10000 and Min:₹100 at a Time",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=150)
    Label(root,text="3.Account Number will be Generated AutoMatically",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=500).place(x=10,y=200)
    Label(root,text="4.You Can Deposit Min:₹100 and Max:₹100000",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=450).place(x=10,y=250)
    Label(root,text="5.You Can Choose Your Own Password but it Can Have 4 Digit",fg="Black",bg="Light blue",font=("Arial Rounded MT Bold",12),wraplength=450).place(x=10,y=300)
    t1=IntVar()
    Radiobutton(root,text="Accept",value=1,variable=t1,fg="Red",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=80,y=360)
    Radiobutton(root,text="Decline",value=0,variable=t1,fg="Red",bg="Light blue",font=("Arial Rounded MT Bold",12)).place(x=300,y=360)
    Button(root,text="Next",command=take,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=400)
    Button(root,text="Home",command=home,activebackground="red",activeforeground="black",fg="cyan",bg="darkblue",width=20).place(x=180,y=450)
    
def home():
    global img1,img2,click_btn,root,amt,k
    root.resizable(0, 0)
    canvas = Canvas(root, width=500, height=450, bd=0, highlightthickness=0, highlightbackground="yellow", bg="light blue")
    canvas.place(x=0,y=0)
    Label(root,text="HOME  PAGE",fg="navy",bg="light blue",font=("Cooper Black" ,20)).place(x=170,y=20)
    Button(root,text="Create Account",command=term,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=100)
    Button(root,text="Login",command=login,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=150)
    Button(root,text="Admin Login",command=ad_login,activebackground="red",activeforeground="black",fg="white",bg="darkblue",width=20).place(x=180,y=200)
    Label(root,text="LAXMI CHIT FUND  BANK",fg="navy",bg="Light blue",font=("Arial Rounded MT Bold",15),width=20).place(x=140,y=250)
k=-1
cl=0
home()
root.mainloop()
