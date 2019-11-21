#line 192
#error at line 195
#for inline 258
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import sys
import os
import string
import sqlite3
import re
def userlogin(widget):
    widget.destroy()
    olduser()
def adminw(widget):
    widget.destroy()
    adminlog()
def fromorderdetails(widget,a_name):
    widget.destroy()
    adminloggedin(a_name)
def orderdetails(a_name):
    ad=Tk()
    ad.title("Admin Screen")
    ad.attributes('-fullscreen',True)
    adwelcome1=Label(ad,text='Welcome to')
    adwelcome2=Label(ad,text='Courier Management System')
    adwelcome1.config(font=('Sans-serif',24,'bold'))
    adwelcome2.config(font=('Script-typeface',30,'bold'))
    adwelcome1.pack()
    adwelcome2.pack()
    adwelcome3=Label(ad,text='Welcome '+a_name)
    adwelcome3.config(font=('Sans-serif',18,'bold'))
    adwelcome3.pack()
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(ad,image=backrender,command=lambda: fromorderdetails(ad,a_name))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(ad,image=exitrender,command=ad.destroy)
    eimg.place(relx=.95,rely=.05)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    addorder=Image.open("D:\\Courier Management System\\Images\\order_add.png")
    addorderrender =ImageTk.PhotoImage(addorder)
    aorderimg = Label(image=addorderrender)
    aorderimg.image = addorderrender
    aorderimg.place(relx=.5, rely=.25 ,anchor=CENTER)
    p_no=Label(ad,text='Phone No')
    p_no.place(relx=.45,rely=.4,anchor=CENTER)
    phone1=IntVar()
    phone=Entry(ad)
    phone.place(relx=.55,rely=.4,anchor=CENTER)
    address=Label(ad,text='Address')
    address.place(relx=.45,rely=.5,anchor=CENTER)
    address1=StringVar()
    addresse=Entry(ad)
    addresse.place(relx=.55,rely=.5,anchor=CENTER)
    def submitnew():
        z=1
        phone1=phone.get()
        try:
            phone11=int(phone1)
        except:
            phone11=0
        if phone11<=999999999 or phone11>9999999999:
            messagebox.showerror("Phone No","Invalid Phone No")
            z=0
        address11=str(addresse.get()).strip()
        if len(address11)>=250:
            messagebox.showerror("Address","Address too long")
            z=0
        OID=0
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('select oid from orderdetail where oid=(select max(oid) from orderdetail)')
        POID=c.fetchone()
        try:
            OID=int(POID[0])+1
        except:
            OID=1
        c.execute('insert into orderdetail(oid,mob_no,address,status) values("%s","%s","%s","%s")'%(OID,phone11,address11,'P'))
        con.commit()
        con.close()
        messagebox.showinfo("Order ID","Order ID is "+str(OID))
        if z==1:
            ad.destroy()
            orderdetails(a_name)
    submit=Button(ad,text="Submit",command= submitnew)
    submit.place(relx=.5,rely=.62,anchor=CENTER)
    ad.mainloop()
def updatew(widget,a_name):
    widget.destroy()
    updatestatus(a_name)
def updatestatus(a_name):
    ad=Tk()
    ad.title("Status Update")
    ad.attributes('-fullscreen',True)
    adwelcome1=Label(ad,text='Welcome to')
    adwelcome2=Label(ad,text='Courier Management System')
    adwelcome1.config(font=('Sans-serif',24,'bold'))
    adwelcome2.config(font=('Script-typeface',30,'bold'))
    adwelcome1.pack()
    adwelcome2.pack()
    adwelcome3=Label(ad,text='Welcome '+a_name)
    adwelcome3.config(font=('Sans-serif',18,'bold'))
    adwelcome3.pack()
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(ad,image=backrender,command=lambda: fromorderdetails(ad,a_name))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(ad,image=exitrender,command=ad.destroy)
    eimg.place(relx=.95,rely=.05)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    addstatus=Image.open("D:\\Courier Management System\\Images\\update.png")
    addstatusrender =ImageTk.PhotoImage(addstatus)
    astatusimg = Label(image=addstatusrender)
    astatusimg.image = astatusimg.place(relx=.5, rely=.25 ,anchor=CENTER)
    p_no=Label(ad,text='Phone No')
    p_no.place(relx=.45,rely=.4,anchor=CENTER)
    phone1=IntVar()
    phone=Entry(ad)
    phone.place(relx=.55,rely=.4,anchor=CENTER)
    take_oid=StringVar()
    getorder=Label(ad,text='Enter Order ID which are Delivered using comma(,)')
    getorder.place(relx=.4,rely=.5,anchor=CENTER)
    enterorder=Entry(ad)
    enterorder.place(relx=.55,rely=.5,anchor=CENTER)
    def showlist():
        z=1
        phone1=phone.get()
        try:
            phone11=int(phone1)
        except:
            phone11=0
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('select * from orderdetail where mob_no="%s"'%(phone11))
        if c.fetchone() is None:
            messagebox.showerror("Not Available","Phone no does not exists")
            z=0
        con.commit()
        con.close()
        if z==1:
            w1=Label(ad,text='Pending Orders')
            w2=Label(ad,text='Delivered Orders')
            #need to updaate
            con=sqlite3.connect("CMS.db")
            c=con.cursor()
            c.execute('select oid,address from orderdetail where mob_no="%s" and status="P"'%(phone11))
            list=c.fetchall()
            scrollbar = Scrollbar(ad)
            scrollbar.place( x=1500,y=200, height=600 )
            mylist = Listbox(ad, yscrollcommand = scrollbar.set )
            i=0
            for line in list:
                mylist.insert(END,str(line[0])+"   "+str(line[1]))
            mylist.place( x=1150,y=200, height=600,width=300 )
            w1.place(x=1280,y=180)
            scrollbar.config( command = mylist.yview )
            con.commit()
            con.close()
            con=sqlite3.connect("CMS.db")
            c=con.cursor()
            c.execute('select oid,address from orderdetail where mob_no="%s" and status="D"'%(phone11))
            list=c.fetchall()
            scrollbar = Scrollbar(ad)
            scrollbar.place( x=0,y=200, height=600 )
            mylist = Listbox(ad, yscrollcommand = scrollbar.set )
            for line in list:
                mylist.insert(END,str(line[0])+"   "+str(line[1]))
            mylist.place( x=50,y=200, height=600,width=300 )
            w2.place(x=180,y=180)
            scrollbar.config( command = mylist.yview )
            con.commit()
            con.close()
    sho=Button(ad,text="Show List",command= showlist)
    sho.place(relx=.65,rely=.4,anchor=CENTER)
    def submitnew():
        take_oid1=enterorder.get()
        take_oid=take_oid1.split(",")
        print(take_oid)
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        messagebox.showinfo("Enter Order ID","Entered Order ID is/are "+str(take_oid))
        for i in take_oid:
            c.execute('update orderdetail set status="D" where oid="%s"'%(int(i)))
            #c.execute('select * from orderdetail where status="D" and oid="%s"'%(i))
            #print(c.fetchone())
        con.commit()
        con.close()
    submit=Button(ad,text="Submit",command= submitnew)
    submit.place(relx=.5,rely=.62,anchor=CENTER)
    ad.mainloop()
def addneworder(widget,a_name):
    widget.destroy()
    orderdetails(a_name)
def addnewadmin(widget,a_name):#need change
    widget.destroy()
    naw=Tk()#newadmin window
    naw.title("Add New Admin Screen")
    naw.attributes('-fullscreen',True)
    logwelcome1=Label(naw,text='Welcome to')
    logwelcome2=Label(naw,text='Courier Management System')
    logwelcome1.config(font=('Sans-serif',24,'bold'))
    logwelcome2.config(font=('Script-typeface',30,'bold'))
    logwelcome1.pack()
    logwelcome2.pack()
    log=Label(naw,text='Add Admin')
    log.config(font=('Script-typeface',30,'bold'))
    log.place(relx=.5,rely=.2,anchor=CENTER)
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(naw,image=backrender,command=lambda: fromorderdetails(naw,a_name))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(naw,image=exitrender,command=naw.destroy)
    eimg.place(relx=.95,rely=.05)
    adminimg=Image.open("D:\\Courier Management System\\Images\\add_admin.png")
    adminrender=ImageTk.PhotoImage(adminimg)
    aimg = Label(image=adminrender)
    aimg.image = adminrender
    aimg.place(relx=.5, rely=.3 ,anchor=CENTER)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    aname=Label(naw,text='Admin ID')
    aname.place(relx=.45,rely=.4,anchor=CENTER)
    adminname=Entry(naw)
    adminname.place(relx=.55,rely=.4,anchor=CENTER)
    adminname.focus_set()#cahange
    pswrd=Label(naw,text='Password')
    pswrd.place(relx=.45,rely=.45,anchor=CENTER)
    password=Entry(show="*")
    password.place(relx=.55,rely=.45,anchor=CENTER)
    def onsubmit():
        text1=adminname.get()
        text2=password.get()
        z=1
        A=1
        adminname1=text1.strip()
        adminname11=str(adminname1)
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('SELECT * from admin WHERE AID="%s"' % (adminname11))
        if (len(adminname11)<4):
            messagebox.showerror("Admin ID","Admin ID should contain atlest 4 character")
            A=0
        elif not re.search("[a-z]", adminname11):
            messagebox.showerror("Admin ID","Admin ID should contain small letter")
            A=0
        elif re.search("[A-Z]", adminname11):
            A=0
            messagebox.showerror("Admin ID","Capital letters are not allowed in Admin ID")
        elif re.search("[@_&%]",adminname11):
            messagebox.showerror("Admin ID","Admin ID should not contain _,@ or $ special letter")
            A=0
        elif re.search("\s", adminname11):
            messagebox.showerror("Admin ID","Admin ID should not contain space")
            A=0
        elif c.fetchone() is not None:
            messagebox.showerror("Not Available","Admin ID already taken Please try another")
            A=0
        con.commit()
        con.close()
        password1=text2.strip()
        password123=str(password1)
        if (len(password123)<8):
            messagebox.showerror("Password","Password should contain atlest 8 character")
            z=0
        elif not re.search("[a-z]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 small letter")
            z=0
        elif not re.search("[A-Z]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 capital letter")
            z=0
        elif not re.search("[0-9]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 small letter")
            z=0
        elif not re.search("[_@$]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 of _,@ or $ special letter")
            z=0
        elif re.search("\s", password123):
            messagebox.showerror("Password","Password should not contain space")
            z=0
        else:
            z=1
        if A==1 and z==1:
            con=sqlite3.connect("CMS.db")
            c=con.cursor()
            c.execute('insert into admin(AID,Password) values(?,?)',(adminname11,password123))
            con.commit()
            con.close()
            messagebox.showinfo("Admin Info","Admin ID:-"+str(adminname11)+"\n Admin Password is"+str(password123))
    submit=Button(naw,text="Add Admin",command= onsubmit)
    submit.place(relx=.45,rely=.5,anchor=CENTER)
    naw.mainloop()
def orderlistw(a_name):
    ad=Tk()
    ad.title("Admin Screen")
    ad.attributes('-fullscreen',True)
    adwelcome1=Label(ad,text='Welcome to')
    adwelcome2=Label(ad,text='Courier Management System')
    adwelcome1.config(font=('Sans-serif',24,'bold'))
    adwelcome2.config(font=('Script-typeface',30,'bold'))
    adwelcome1.pack()
    adwelcome2.pack()
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(ad,image=backrender,command=lambda: fromorderdetails(ad,a_name))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(ad,image=exitrender,command=ad.destroy)
    eimg.place(relx=.95,rely=.05)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    adwelcome3=Label(ad,text='Welcome '+a_name)
    adwelcome3.config(font=('Sans-serif',18,'bold'))
    adwelcome3.pack()
    label1=Label(ad,text="Delivered Orders")
    label2=Label(ad,text="Pending Orders")
    con=sqlite3.connect("CMS.db")
    c=con.cursor()
    c.execute('select * from orderdetail where status="P"')
    list=c.fetchall()
    scrollbar = Scrollbar(ad)
    scrollbar.place( x=1500,y=200, height=600 )
    mylist = Listbox(ad, yscrollcommand = scrollbar.set )
    for line in list:
        mylist.insert(END,str(line[0])+"   "+str(line[1])+"   "+str(line[2]))
    mylist.place( x=1150,y=200, height=600,width=300 )
    label2.place(x=1280,y=180)
    scrollbar.config(command = mylist.yview )
    con.commit()
    con.close()
    con=sqlite3.connect("CMS.db")
    c=con.cursor()
    c.execute('select * from orderdetail where status="D"')
    list=c.fetchall()
    scrollbar = Scrollbar(ad)
    scrollbar.place( x=0,y=200, height=600 )
    mylist = Listbox(ad, yscrollcommand = scrollbar.set )
    for line in list:
        mylist.insert(END,str(line[0])+"   "+str(line[1])+"   "+str(line[2]))
    mylist.place( x=50,y=200, height=600,width=300 )
    label1.place(x=180,y=180)
    scrollbar.config( command = mylist.yview )
    con.commit()
    con.close()
    ad.mainloop()
def orderlist(widget,a_name):
    widget.destroy()
    orderlistw(a_name)
def adminloggedin(adminid):
    a_name=str(adminid).strip()
    ad=Tk()
    ad.title("Admin Screen")
    ad.attributes('-fullscreen',True)
    adwelcome1=Label(ad,text='Welcome to')
    adwelcome2=Label(ad,text='Courier Management System')
    adwelcome1.config(font=('Sans-serif',24,'bold'))
    adwelcome2.config(font=('Script-typeface',30,'bold'))
    adwelcome1.pack()
    adwelcome2.pack()
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(ad,image=backrender,command=lambda: adminw(ad))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(ad,image=exitrender,command=ad.destroy)
    eimg.place(relx=.95,rely=.05)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    adwelcome3=Label(ad,text='Welcome '+a_name)
    adwelcome3.config(font=('Sans-serif',18,'bold'))
    adwelcome3.pack()
    addorder=Image.open("D:\\Courier Management System\\Images\\order_add.png")
    addorderrender =ImageTk.PhotoImage(addorder)
    aorderimg = Label(image=addorderrender)
    aorderimg.image = addorderrender
    aorderimg.place(relx=.2, rely=.25 ,anchor=CENTER)
    addorderButton=Button(ad,text="Add new Order",command=lambda: addneworder(ad,a_name))
    addorderButton.place(relx=.2,rely=.33,anchor=CENTER)
    addstatus=Image.open("D:\\Courier Management System\\Images\\update.png")
    addstatusrender =ImageTk.PhotoImage(addstatus)
    astatusimg = Label(image=addstatusrender)
    astatusimg.image = addstatusrender
    astatusimg.place(relx=.5, rely=.25 ,anchor=CENTER)
    addstatusButton=Button(ad,text="Update Order",command=lambda: updatew(ad,a_name))
    addstatusButton.place(relx=.5,rely=.33,anchor=CENTER)
    pending=Image.open("D:\\Courier Management System\\Images\\detail.png")
    pendingrender =ImageTk.PhotoImage(pending)
    pendingimg = Label(image=pendingrender)
    pendingimg.image = pendingrender
    pendingimg.place(relx=.8, rely=.25 ,anchor=CENTER)
    pendingButton=Button(ad,text="Orders",command=lambda: orderlist(ad,a_name))#new fun pending
    pendingButton.place(relx=.8,rely=.33,anchor=CENTER)
    addadmin=Image.open("D:\\Courier Management System\\Images\\add_admin.png")
    addadminrender =ImageTk.PhotoImage(addadmin)
    aadminimg = Label(image=addadminrender)
    aadminimg.image = addadminrender
    aadminimg.place(relx=.35, rely=.55 ,anchor=CENTER)
    addadminButton=Button(ad,text="Add new Admin",command=lambda: addnewadmin(ad,a_name))
    addadminButton.place(relx=.35,rely=.63,anchor=CENTER)
    reset=Image.open("D:\\Courier Management System\\Images\\forgot_password.png")
    resetrender =ImageTk.PhotoImage(reset)
    resetimg = Label(image=resetrender)
    resetimg.image = resetrender
    resetimg.place(relx=.65, rely=.55 ,anchor=CENTER)
    resetButton=Button(ad,text="Reset Password",command="#")#new fun pending
    resetButton.place(relx=.65,rely=.63,anchor=CENTER)
    more=Image.open("D:\\Courier Management System\\Images\\more.png")
    morerender =ImageTk.PhotoImage(more)
    moreimg = Label(image=morerender)
    moreimg.image = morerender
    moreimg.place(relx=.5, rely=.77 ,anchor=CENTER)
    moreButton=Button(ad,text="More",command="#")#new fun pending
    moreButton.place(relx=.5,rely=.85,anchor=CENTER)
    ad.mainloop()
def adminlog():
    ad=Tk()
    ad.title("Admin Screen")
    ad.attributes('-fullscreen',True)
    adwelcome1=Label(ad,text='Welcome to')
    adwelcome2=Label(ad,text='Courier Management System')
    adwelcome1.config(font=('Sans-serif',24,'bold'))
    adwelcome2.config(font=('Script-typeface',30,'bold'))
    adwelcome1.pack()
    adwelcome2.pack()
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(ad,image=backrender,command=lambda: back(ad))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(ad,image=exitrender,command=ad.destroy)
    eimg.place(relx=.95,rely=.05)
    adminimg=Image.open("D:\\Courier Management System\\Images\\Admin.png")
    adminrender =ImageTk.PhotoImage(adminimg)
    aimg = Label(image=adminrender)
    aimg.image = adminrender
    aimg.place(relx=.5, rely=.3 ,anchor=CENTER)
    aname=Label(ad,text='AdminID')
    aname.place(relx=.45,rely=.4,anchor=CENTER)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    adminname=Entry(ad)
    adminname.place(relx=.55,rely=.4,anchor=CENTER)
    adminname.focus_set()
    pswrd=Label(ad,text='Password')
    pswrd.place(relx=.45,rely=.45,anchor=CENTER)
    password=Entry(ad,show="*")#
    password.place(relx=.55,rely=.45,anchor=CENTER)
    def onsubmit():
        an=adminname.get()
        ans=str(an)
        ps=password.get()
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('SELECT * from admin WHERE AID="%s" AND Password="%s"' % (an,ps))
        if c.fetchone() is not None:
            ad.destroy()
            adminloggedin(ans)#after login through admin window
        else:
            loginprompt()
        con.commit()
        con.close()
    def default():
        messagebox.showwarning("Reset","Admin and Password reset to default for more ask the developer")
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('delete from admin where AID="%s"'%("admin"))
        c.execute('select * from admin')
        if c.fetchone() is None:
            c.execute('insert into admin(AID,Password) values("%s","%s")'%("admin","Admin@123"))
        con.commit()
        con.close()
    forgot=Button(ad,text="Reset Password",command= default)
    forgot.place(relx=.45,rely=.50,anchor=CENTER)
    submit=Button(ad,text="Login",command= onsubmit)
    submit.place(relx=.55,rely=.50,anchor=CENTER)
    ad.mainloop()
def mainscreen():
    ms=Tk()
    ms.title("Home Screen")
    ms.attributes('-fullscreen',True)
    con=sqlite3.connect("CMS.db")
    c=con.cursor()
    c.execute('create table if not exists user(username varchar(25) Primary Key,Password varchar(15) NOT NULL)')
    c.execute('create table if not exists userdetail(username Foriegn Key refrences user,f_name varchar(20) not null,m_name varchar(20),l_name varchar(20),gender char(1),reg_no number(8),mob_no number(10),emailid varchar(250))')
    c.execute('create table if not exists orderdetail(oid int Primary Key,mob_no number(8),address varchar(250),status char(1))')
    c.execute('create table if not exists admin(AID varchar(25) Primary Key,Password varchar(15) NOT NULL)')
    con.commit()
    con.close()
    mswelcome1=Label(ms,text='Welcome')
    mswelcome2=Label(ms,text='Courier Management System')
    mswelcome1.config(font=('Sans-serif',24,'bold'))
    mswelcome2.config(font=('Script-typeface',30,'bold'))
    mswelcome1.pack()
    mswelcome2.pack()
    userbtn=Button(ms,text="User",command=lambda: userlogin(ms))
    adminbtn=Button(ms,text="Admin",command=lambda: adminw(ms))
    userimg=Image.open("D:\\Courier Management System\\Images\\User.png")
    userrender=ImageTk.PhotoImage(userimg)
    adminimg=Image.open("D:\\Courier Management System\\Images\\Admin.png")
    adminrender=ImageTk.PhotoImage(adminimg)
    uimg = Label(image=userrender)
    uimg.image = userrender
    aimg = Label(image=adminrender)
    aimg.image =adminrender
    aimg.place(relx=.75,rely=.4,anchor=CENTER)
    trackimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    trackrender=ImageTk.PhotoImage(trackimg)
    timg = Label(image=trackrender)
    timg.image = trackrender
    timg.place(relx=.5, rely=.4 ,anchor=CENTER)
    def passtrack():
        ms.destroy()
        trackw()
    track=Button(ms,text="Track Consignment",command= passtrack)
    track.place(relx=.5,rely=.5,anchor=CENTER)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    uimg.place(relx=.25, rely=.4 ,anchor=CENTER)
    userbtn.place(relx=.25,rely=.5,anchor=CENTER)
    adminbtn.place(relx=.75,rely=.5,anchor=CENTER)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(image=exitrender,command=ms.destroy)
    eimg.place(relx=.5,rely=.63,anchor=CENTER)
    exitButton=Button(ms,text="Exit Program",command=ms.destroy)
    exitButton.place(relx=.5,rely=.73,anchor=CENTER)
    ms.mainloop()
def back(widget):
    widget.destroy()
    mainscreen()
def loginprompt():
    messagebox.showwarning('WARNING','Please enter valid username and password')
def login(u,p,k):
    username=u
    password=p
    con=sqlite3.connect("CMS.db")
    c=con.cursor()
    c.execute('SELECT * from user WHERE username="%s" AND Password="%s"' % (username, password))
    if c.fetchone() is not None:
        k.destroy()
        afterlogin()
    else:
        loginprompt()
    con.commit()
    con.close()
def olduser():
    loginw=Tk()
    loginw.title("Login Screen")
    loginw.attributes('-fullscreen',True)
    logwelcome1=Label(loginw,text='Welcome to')
    logwelcome2=Label(loginw,text='Courier Management System')
    logwelcome1.config(font=('Sans-serif',24,'bold'))
    logwelcome2.config(font=('Script-typeface',30,'bold'))
    logwelcome1.pack()
    logwelcome2.pack()
    log=Label(loginw,text='User Login')
    log.config(font=('Script-typeface',30,'bold'))
    log.place(relx=.5,rely=.2,anchor=CENTER)
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(loginw,image=backrender,command=lambda: back(loginw))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(loginw,image=exitrender,command=loginw.destroy)
    eimg.place(relx=.95,rely=.05)
    userimg=Image.open("D:\\Courier Management System\\Images\\User.png")
    userrender=ImageTk.PhotoImage(userimg)
    uimg = Label(image=userrender)
    uimg.image = userrender
    uimg.place(relx=.5, rely=.3 ,anchor=CENTER)
    uname=Label(loginw,text='Username')
    uname.place(relx=.45,rely=.4,anchor=CENTER)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    username=Entry(loginw)
    username.place(relx=.55,rely=.4,anchor=CENTER)
    username.focus_set()
    pswrd=Label(loginw,text='Password')
    pswrd.place(relx=.45,rely=.45,anchor=CENTER)
    password=Entry(show="*")
    password.place(relx=.55,rely=.45,anchor=CENTER)
    def onsubmit():
        text1=username.get()
        text2=password.get()
        login(text1,text2,loginw)
    def passnew():
        loginw.destroy()
        newuserw()
    def passtrack():
        loginw.destroy()
        trackw()
    submit=Button(loginw,text="Login",command= onsubmit)
    newuser=Button(loginw,text="New User",command= passnew)
    track=Button(loginw,text="Track Consignment",command= passtrack)
    submit.place(relx=.45,rely=.5,anchor=CENTER)
    track.place(relx=.52,rely=.55,anchor=CENTER)
    newuser.place(relx=.57,rely=.5,anchor=CENTER)
    loginw.mainloop()
def afterlogin():
    print("Welcome to login window")
def newdatauser(username,password,firstname,middlename,lastname,email,gender,phone,reg):
    print("Welcome now your data will be saved")
    con=sqlite3.connect("CMS.db")
    c=con.cursor()
    c.execute('insert into user(username,Password) values("%s","%s")'%(username,password))
    c.execute('insert into userdetail(username,f_name,m_name,l_name,gender,reg_no,mob_no,emailid) values("%s","%s","%s","%s","%s","%s","%s","%s")'%(username,firstname,middlename,lastname,gender,reg,phone,email))
    con.commit()
    con.close()
def back1(widget):
    widget.destroy()
    olduser()
def newuserw():
    new=Tk()
    new.title("Register")
    new.attributes('-fullscreen',True)
    logwelcome1=Label(new,text='Welcome to')
    logwelcome2=Label(new,text='Courier Management System')
    logwelcome1.config(font=('Sans-serif',24,'bold'))
    logwelcome2.config(font=('Script-typeface',30,'bold'))
    logwelcome1.pack()
    logwelcome2.pack()
    log=Label(new,text='Register New User')
    log.config(font=('Script-typeface',30,'bold'))
    log.place(relx=.5,rely=.2,anchor=CENTER)
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(new,image=backrender,command=lambda: back1(new))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(new,image=exitrender,command=new.destroy)
    eimg.place(relx=.95,rely=.05)
    logoimg=Image.open("D:\\Courier Management System\\Images\\transit.png")
    logorender=ImageTk.PhotoImage(logoimg)
    lgimg = Label(image=logorender)
    lgimg.image=logorender
    lgimg.place(relx=.05,rely=.052,anchor=CENTER)
    userimg=Image.open("D:\\Courier Management System\\Images\\User.png")
    userrender=ImageTk.PhotoImage(userimg)
    uimg = Label(image=userrender)
    uimg.image = userrender
    uimg.place(relx=.5, rely=.3 ,anchor=CENTER)
    uname=Label(new,text='Username')
    uname.place(relx=.45,rely=.4,anchor=CENTER)
    username1=StringVar()#for getttin username
    username=Entry(new)
    username.place(relx=.55,rely=.4,anchor=CENTER)
    username.focus_set()
    pswrd=Label(new,text='Password')
    pswrd.place(relx=.45,rely=.45,anchor=CENTER)
    password11=StringVar()#for getting password
    password=Entry(show="*")
    password.place(relx=.55,rely=.45,anchor=CENTER)
    pswrd1=Label(new,text='Re-enter Password')
    pswrd1.place(relx=.45,rely=.47,anchor=CENTER)
    password12=StringVar()#for getting password check
    password1=Entry(show="*")
    password1.place(relx=.55,rely=.47,anchor=CENTER)
    f_name=Label(new,text='First Name')
    f_name.place(relx=.45,rely=.52,anchor=CENTER)
    firstname1=StringVar()#for getting firstname
    firstname=Entry(new)
    firstname.place(relx=.55,rely=.52,anchor=CENTER)
    m_name=Label(new,text='Middle Name')
    m_name.place(relx=.45,rely=.54,anchor=CENTER)
    middlename1=StringVar()#for getting middle name
    middlename=Entry(new)
    middlename.place(relx=.55,rely=.54,anchor=CENTER)
    l_name=Label(new,text='Last Name')
    l_name.place(relx=.45,rely=.56,anchor=CENTER)
    lastname1=StringVar()#for getting lastname
    lastname=Entry(new)
    lastname.place(relx=.55,rely=.56,anchor=CENTER)
    e_mail=Label(new,text='E-Mail ID')
    e_mail.place(relx=.45,rely=.61,anchor=CENTER)
    email1=StringVar()#for getting email
    email=Entry(new)
    email.place(relx=.55,rely=.61,anchor=CENTER)
    def genders():
        selection= var.get()
        if selection==3:
            return 'O'
        elif selection==2:
            return 'F'
        else:
            return 'M'
    var = IntVar()
    gender=Label(new,text='Gender')
    gender.place(relx=.45,rely=.64,anchor=CENTER)
    R1 = Radiobutton(new, text="M", variable=var, value=1,command=genders)
    R1.place(relx=.52,rely=.64,anchor=CENTER)
    R1.focus_set()##already select option nhi hua abhi
    R2 = Radiobutton(new, text="F", variable=var, value=2,command=genders)
    R2.place(relx=.555,rely=.64,anchor=CENTER)
    R3 = Radiobutton(new, text="O", variable=var, value=3,command=genders)
    R3.place(relx=.58,rely=.64,anchor=CENTER)
    p_no=Label(new,text='Phone No')
    p_no.place(relx=.45,rely=.69,anchor=CENTER)
    phone1=IntVar()
    phone=Entry(new)
    phone.place(relx=.55,rely=.69,anchor=CENTER)
    r_no=Label(new,text='Registration No')
    r_no.place(relx=.45,rely=.73,anchor=CENTER)
    reg1=IntVar()
    reg=Entry(new)
    reg.place(relx=.55,rely=.73,anchor=CENTER)
    def submitnew():
        z=1
        A=1
        username1=username.get()
        username1=username1.strip()
        username11=str(username1)
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('SELECT * from user WHERE username="%s"' % (username11))
        if (len(username11)<4):
            z=0
            messagebox.showerror("Username","Username should contain atlest 4 character")
            A=0
        elif not re.search("[a-z]", username11):
            messagebox.showerror("Username","Username should contain small letter")
            z=0
        elif re.search("[A-Z]", username11):
            A=0
            messagebox.showerror("Username","Capital letters are not allowed in username")
        elif re.search("[@_&%]",username11):
            messagebox.showerror("Username","Username should not contain _,@ or $ special letter")
            z=0
        elif re.search("\s", username11):
            messagebox.showerror("Username","Username should not contain space")
            z=0
        elif c.fetchone() is not None:
            messagebox.showerror("Not Available","Username already taken Please try another")
            z=0
        con.commit()
        con.close()
        password11=password.get()
        password12=password1.get()
        password11=password11.strip()
        password12=password12.strip()
        password123=str(password12)
        if (len(password123)<8):
            messagebox.showerror("Password","Password should contain atlest 8 character")
            z=0
        elif not re.search("[a-z]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 small letter")
            z=0
        elif not re.search("[A-Z]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 capital letter")
            z=0
        elif not re.search("[0-9]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 small letter")
            z=0
        elif not re.search("[_@$]", password123):
            messagebox.showerror("Password","Password should contain atlest 1 of _,@ or $ special letter")
            z=0
        elif re.search("\s", password123):
            messagebox.showerror("Password","Password should not contain space")
            z=0
        else:
            z=1
        if password11=="" or password12=="":
            messagebox.showerror("Blank","Please enter password")
            z=0
        if password11!=password12:
            messagebox.showerror("Password not match","Please enter password again")
            z=0
        firstname1=firstname.get()
        firstname1=firstname1.strip()
        firstname11=str(firstname1)
        if firstname1=="":
            messagebox.showerror("Blank","First Name Cann't be leave blank")
            z=0
        if re.search("[_@$]",firstname11):
            messagebox.showerror("Name","First name should not contain _,@ or $ special letter")
            z=0
        else:
            if re.search("[0-9]",firstname11):
                messagebox.showerror("Name","First name should not contain digit")
                z=0
        middlename1=middlename.get()
        middlename1=middlename1.strip()
        middlename11=str(middlename1)
        if re.search("[_@$]",middlename11):
            messagebox.showerror("Name","Middle name should not contain _,@ or $ special letter")
            z=0
        else:
            if re.search("[0-9]",middlename11):
                messagebox.showerror("Name","Middle name should not contain digit")
                z=0
        lastname1=lastname.get()
        lastname1=lastname1.strip()
        lastname11=str(lastname1)
        if re.search("[_@$]",lastname11):
            messagebox.showerror("Name","Last name should not contain _,@ or $ special letter")
            z=0
        else:
            if re.search("[0-9]",lastname11):
                messagebox.showerror("Name","Last name should not contain digit")
                z=0
        email1=email.get()
        email1=email1.strip()
        email11=str(email1)#for further validation
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('SELECT * from userdetail WHERE emailid="%s"' % (email11))
        if email11=="":
            messagebox.showerror("Blank","E-Mail Id Cann't be leave blank")
            z=0
        elif not re.search("[@]",email11):
            messagebox.showerror("E-Mail","Invalid E-Mail")
            z=0
        elif not re.search("[.]",email11):
            messagebox.showerror("E-Mail","Invalid E-Mail")
            z=0
        elif email11[-4:]!=".com":
            print(email11[-4:])
            messagebox.showerror("E-Mail","Invalid E-Mail")
            z=0
        elif c.fetchone() is not None:
            messagebox.showerror("Not Available","E-mail already exists")
            z=0
        con.commit()
        con.close()
        gender1=genders()
        gender11=str(gender1)
        phone1=phone.get()
        try:
            phone11=int(phone1)
        except:
            phone11=0
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('SELECT * from userdetail WHERE mob_no="%s"' % (phone11))
        if phone11<=999999999 or phone11>9999999999:
            messagebox.showerror("Phone No","Invalid Phone No")
            z=0
        elif c.fetchone() is not None:
            messagebox.showerror("Not Available","Phone no already exists")
            z=0
        con.commit()
        con.close()
        reg1=reg.get()
        try:
            reg11=int(reg1)
        except:
            reg11=0
        if reg11<=9999999 or reg11>99999999:
            messagebox.showerror("Registration No","Invalid Registration No")
            z=0
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('SELECT * from userdetail WHERE reg_no="%s"' % (reg11))
        if c.fetchone() is not None:
            messagebox.showerror("Not Available","Registration no already exists")
            z=0
        con.commit()
        con.close()
        if z==1 and A==1:
            new.destroy()
            newdatauser(username11,password123,firstname11,middlename11,lastname11,email11,gender11,phone11,reg11)
            olduser()
    submit=Button(new,text="Submit",command= submitnew)
    backl=Button(new,text="Login",command=lambda: back1(new))
    submit.place(relx=.57,rely=.78,anchor=CENTER)
    backl.place(relx=.47,rely=.78,anchor=CENTER)
    new.mainloop()
def trackw():
    '''tw=Tk()
    tw.title("Track")
    tw.attributes('-fullscreen',True)
    logwelcome1=Label(loginw,text='Welcome to')
    logwelcome2=Label(loginw,text='Courier Management System')
    logwelcome1.config(font=('Sans-serif',24,'bold'))
    logwelcome2.config(font=('Script-typeface',30,'bold'))
    logwelcome1.pack()
    logwelcome2.pack()
    log=Label(loginw,text='Track Consignment')
    log.config(font=('Script-typeface',30,'bold'))
    log.place(relx=.5,rely=.2,anchor=CENTER)
    backimg=Image.open("D:\\Courier Management System\\Images\\Back.png")
    backrender=ImageTk.PhotoImage(backimg)
    bimg=Button(loginw,image=backrender,command=lambda: back(loginw))
    bimg.image=backrender
    bimg.place(relx=.9,rely=.05)
    exitimg=Image.open("D:\\Courier Management System\\Images\\Exit1.png")
    exitrender=ImageTk.PhotoImage(exitimg)
    eimg=Button(loginw,image=exitrender,command=loginw.destroy)
    eimg.place(relx=.95,rely=.05)
    userimg=Image.open("D:\\Courier Management System\\Images\\User.png")
    userrender=ImageTk.PhotoImage(userimg)
    uimg = Label(image=userrender)
    uimg.image = userrender
    uimg.place(relx=.5, rely=.3 ,anchor=CENTER)'''

mainscreen()
