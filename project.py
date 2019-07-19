

#-----------------------------------Login---------------------------------------------------------------------------#


from tkinter import *
from tkinter import Tk, StringVar, ttk, LabelFrame, Scrollbar
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
import budget_backend
import pandas as pd


import numpy as np         #it is used for array

import random
import time
import datetime

import tkinter.messagebox
import mysql.connector as ms
obj=tkinter.Tk()
def obj2():
    obj=tkinter.Tk()
    obj.geometry("1920x1080+0+0")
    obj.title("BUDGET")


    obj.configure(background="maroon")

    Tops = Frame(obj,width=1920,height=90,bg="Black",bd=14, relief=GROOVE)
    Tops.pack(side=TOP)
    f1=Frame(obj,width=300,height=69,bg="red",relief=GROOVE)
    f1.place(x=10,y=10)
    photo2 = PhotoImage(file="home4.png")
    label = Label(obj, image=photo2)
    label.place(x=350, y=120)
    Label(f1,text="HOME BUDGET",bg="red",fg="white",height=1,width=15,font=("Times 16 bold",25,"italic")).place(x=15,y=15)

    f2 = Frame(obj,width=350,height=700,bd=8,relief=GROOVE,bg="black")
    f2.pack(side=LEFT)
    photo=PhotoImage(file="dollar3.png")
    label=Label(f2,image=photo)
    label.place(x=1,y=102)
    photo1=PhotoImage(file="expense1.png")
    label=Label(f2,image=photo1)
    label.place(x=1,y=202)
    photo3 = PhotoImage(file="exp_cat1.png")
    label = Label(f2, image=photo3)
    label.place(x=1, y=302)
    photo4= PhotoImage(file="user.png")
    label = Label(f2, image=photo4)
    label.place(x=1, y=402)


    def search():

        InID = Variable()
        Catname = StringVar()
        Amt = Variable()
        DoB=StringVar()

        # --------------------Functions------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("Home Budget Management", "Confirm if you want to exit")
            if iExit > 0:
                obj.destroy()
                return

        def clearData():
            txtInID.delete(0, END)   #for clear purpose we use (0,END)
            txtDoB.delete(0,END)
            txtCn.delete(0, END)
            txtAm.delete(0, END)
            #categorylist.delete(0, END)

        def addData():
            if ((InID.get() != 0)):
                budget_backend.addIncCat(InID.get(),DoB.get(), Catname.get(), Amt.get())
                categorylist.delete(0, END)
                categorylist.insert(END, (InID.get(),DoB.get(), Catname.get(), Amt.get()))

        def viewData():
            categorylist.delete(0, END)
            for row in budget_backend.viewIncData():
                categorylist.insert(END, row, str(""))

        def IncomeRec(event):
            global In
            searchData = categorylist.curselection()
            In = categorylist.get(searchData)

            txtInID.delete(0, END)
            txtInID.insert(END, In[0])
            txtDoB.delete(0,END)
            txtDoB.insert(END,In[1])
            txtCn.delete(0, END)
            txtCn.insert(END, In[2])
            txtAm.delete(0, END)
            txtAm.insert(END, In[3])

        def deleteData():
            if ((InID.get() != 0)):
                budget_backend.deleteIncData(InID.get())
            clearData()
            viewData()

        def searchData():
            categorylist.delete(0, END)
            for row in budget_backend.searchIncData(InID.get(),DoB.get(), Catname.get(), Amt.get()):
                categorylist.insert(END, row, str(""))

        def update():
            if (InID.get() != 0):
                budget_backend.deleteIncData(InID.get())
            if (InID.get() != 0):
                budget_backend.addIncCat(InID.get(),DoB.get(), Catname.get(), Amt.get())
                categorylist.delete(0, END)
                categorylist.insert(END, (InID.get(),DoB.get(), Catname.get(), Amt.get()))

        Imf = Frame(obj, height=700, width=1400, bg="firebrick4", relief=RAISED).place(x=350, y=95)
        # Imf.grid()

        imf1 = Frame(Imf, bd=2, padx=54, pady=8, bg="tomato", relief=RIDGE)
        imf1.place(x=680,y=95)
        # imf1.pack(side=TOP)

        lblim = Label(imf1, font=('arial', 25, 'bold'), text="Income Management", bg="Ghost White", fg="black")
        lblim.grid()

        ButtonFrame = Frame(Imf, bd=2, width=1500, height=160, padx=18, pady=10, bg="red1", relief=RIDGE)
        ButtonFrame.place(x=370,y=160)

        DataFrame = Frame(Imf, bd=2, width=1450, height=10, padx=20, pady=20, relief=RIDGE, bg="tomato")
        DataFrame.place(x=360,y=260)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=700, height=100, padx=20, relief=RIDGE, bg="Ghost White",
                                   font=('arial', 20, 'bold'), text="Income Category")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=500, height=50, padx=31, pady=3, relief=RIDGE,
                                    bg="Ghost White",
                                    font=('arial', 20, 'bold'), text="Income Details")
        DataFrameRight.pack(side=RIGHT)

        # ----------------------------Labels--------------------------------------#

        lblInID = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Income ID:", padx=2, pady=2, bg="Ghost White")
        lblInID.grid(row=0, column=0, sticky=W)
        txtInID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=InID, width=39)
        txtInID.grid(row=0, column=1)

        lblDoB = Label(DataFrameLeft, font=('arial', 15, 'bold'), text="Date:[YYYY-MM-DD]", padx=1, pady=1, bg="Ghost White")
        lblDoB.grid(row=1, column=0, sticky=W)
        txtDoB = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        txtDoB.grid(row=1, column=1)

        lblCn = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Category:", padx=2, pady=2, bg="Ghost White")
        lblCn.grid(row=2, column=0, sticky=W)
        txtCn = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Catname, width=39)
        txtCn.grid(row=2, column=1)

        lblAm = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Amount:", padx=2, pady=2, bg="Ghost White")
        lblAm.grid(row=3, column=0, sticky=W)
        txtAm = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Amt, width=39)
        txtAm.grid(row=3, column=1)



        # --------------------------ListBox & ScrollBar-------------
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        categorylist = Listbox(DataFrameRight, width=38, height=15, font=('arial', 12, 'bold'),
                               yscrollcommand=scrollbar.set)
        categorylist.bind('<<ListboxSelect>>', IncomeRec)
        categorylist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=categorylist.yview)

        # -----------------Button--------------------------------------

        btnAdd = Button(ButtonFrame, text="Add", font=("arial", 20, 'bold'), height=1, width=10, bd=4, command=addData)
        btnAdd.grid(row=0, column=0)

        btnSearch = Button(ButtonFrame, text="Search", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                           command=searchData)
        btnSearch.grid(row=0, column=1)

        btnView = Button(ButtonFrame, text="View", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                         command=viewData)
        btnView.grid(row=0, column=2)

        btnEdit = Button(ButtonFrame, text="Edit", font=("arial", 20, 'bold'), height=1, width=10, bd=4, command=update)
        btnEdit.grid(row=0, column=3)

        btnDel = Button(ButtonFrame, text="Delete", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                        command=deleteData)
        btnDel.grid(row=0, column=4)

        btnClear = Button(ButtonFrame, text="Clear", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                          command=clearData)
        btnClear.grid(row=0, column=5)

    Button(f2, text="INCOME CATEGORY", font=("Times", "10", "bold italic"), height=5, width=39, fg="White", bg="RED",
           relief=SOLID, command=search).place(x=45, y=100)

    # -----------------------------Expenses Category--------------------------------------------------#

    def find():
        DoB = Variable()
        ExTd = Variable()
        GROCERY = Variable()
        MEDICINES = Variable()
        FUEL = Variable()
        CLOTHES = Variable()
        ENTERTAINMENT = Variable()
        ELECTRICITY = Variable()
        TOTAL_AMOUNT = Variable()

        # --------------------Functions------------------------
        def clearData1():

            txtDate.delete(0, END)
            txtCn1.delete(0, END)
            txtCn2.delete(0, END)
            txtCn3.delete(0, END)
            txtCn4.delete(0, END)
            txtCn5.delete(0, END)
            txtCn6.delete(0, END)
            txtAm.delete(0, END)

        def call_result():
            num1 = (txtCn1.get())
            num2 = (txtCn2.get())
            num3 = (txtCn3.get())
            num4 = (txtCn4.get())
            num5 = (txtCn5.get())
            num6 = (txtCn6.get())
            result = (int(num1) + int(num2) + int(num3) + int(num4) + int(num5) + int(num6))
            txtAm.insert(0, result)

        def AddData1():
            if (DoB != 0):
                num1 = (txtCn1.get())
                num2 = (txtCn2.get())
                num3 = (txtCn3.get())
                num4 = (txtCn4.get())
                num5 = (txtCn5.get())
                num6 = (txtCn6.get())
                result = (int(num1) + int(num2) + int(num3) + int(num4) + int(num5) + int(num6))
                txtAm.insert(0, result)

                budget_backend.addExpCat(budget_backend.lastId(), DoB.get(), GROCERY.get(), MEDICINES.get(), FUEL.get(),
                                         CLOTHES.get(), ENTERTAINMENT.get(), ELECTRICITY.get(), TOTAL_AMOUNT.get())
                categorylist.delete(0, END)
                categorylist.insert(END, (
                budget_backend.lastId(), DoB.get(), GROCERY.get(), MEDICINES.get(), FUEL.get(), CLOTHES.get(),
                ENTERTAINMENT.get(), ELECTRICITY.get(), TOTAL_AMOUNT.get()))

                clearData1()

        def viewData1():
            categorylist.delete(0, END)
            for row in budget_backend.viewExpData():
                categorylist.insert(END, row, str(""))

        def ExpenseRec(event):
            global Ex
            searchData1 = categorylist.curselection()
            Ex = categorylist.get(searchData1)

            # txtCn0.delete(0, END)
            # txtCn0.insert(END, In[0])
            # txtCn0.insert(budget_backend.lastId() + 1)
            txtCn1.delete(0, END)
            txtCn1.insert(END, In[1])
            txtCn2.delete(0, END)
            txtCn2.insert(END, In[2])
            txtCn3.delete(0, END)
            txtCn3.insert(END, In[3])
            txtCn4.delete(0, END)
            txtCn4.insert(END, In[4])
            txtCn5.delete(0, END)
            txtCn5.insert(END, In[5])
            txtCn6.delete(0, END)
            txtCn6.insert(END, In[6])
            txtAm.delete(0, END)
            txtAm.insert(END, In[7])

        def deleteData1():
            if ((DoB.get() != 0)):
                budget_backend.deleteExpData(DoB.get())
            clearData1()
            viewData1()

        def searchData1():
            categorylist.delete(0, END)
            for row in budget_backend.searchExpData(DoB.get()):
                categorylist.insert(END, row, str(""))

        Imf2 = Frame(obj, height=700, width=1400, bg="firebrick4", relief=RAISED).place(x=350, y=95)
        # Imf.grid()

        imf2 = Frame(Imf2, bd=2, padx=54, pady=8, bg="tomato", relief=RIDGE)
        imf2.place(x=680,y=95)
        # imf2.pack(side=TOP)

        lblim = Label(imf2, font=('arial', 25, 'bold'), text="Expense Management", bg="white", fg="black")
        lblim.grid()

        ButtonFrame = Frame(Imf2, bd=2, width=1500, height=160, padx=18, pady=10, bg="red1", relief=RIDGE)
        ButtonFrame.place(x=370,y=160)

        DataFrame = Frame(Imf2, bd=2, width=1450, height=10, padx=20, pady=20, relief=RIDGE, bg="tomato")
        DataFrame.place(x=360,y=260)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=700, height=100, padx=20, relief=RIDGE, bg="Ghost White",
                                   font=('arial', 20, 'bold'), text="EXPENSES Category")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=500, height=50, padx=31, pady=3, relief=RIDGE,bg="Ghost White",
                                    font=('arial', 20, 'bold'), text="Expenses Details")
        DataFrameRight.pack(side=RIGHT)

        # ----------------------------Labels--------------------------------------#

        lblDate = Label(DataFrameLeft, font=('arial', 15, 'bold'), text="Date[YYYY-MM-DD]:", padx=2, pady=2, bg="Ghost White")
        lblDate.grid(row=0, column=0, sticky=W)
        txtDate = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        txtDate.grid(row=0, column=1)

        lblCn = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Category:", padx=2, pady=2, bg="Ghost White")
        lblCn.grid(row=1, column=0, sticky=W)
        #
        # lblCn0 = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="ID", padx=2, pady=2, bg="Ghost White")
        # lblCn0.grid(row=2, column=0, sticky=W)
        # txtCn0 = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=ExTd, width=39)
        # txtCn0.grid(row=2, column=1)

        lblCn1 = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="*Grocery", padx=2, pady=2, bg="Ghost White")
        lblCn1.grid(row=3, column=0, sticky=W)
        txtCn1 = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=GROCERY, width=39)
        txtCn1.grid(row=3, column=1)

        lblCn2 = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="*Medicines", padx=2, pady=2, bg="Ghost White")
        lblCn2.grid(row=4, column=0, sticky=W)
        txtCn2 = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=MEDICINES, width=39)
        txtCn2.grid(row=4, column=1)

        lblCn3 = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="*Fuel", padx=2, pady=2, bg="Ghost White")
        lblCn3.grid(row=5, column=0, sticky=W)
        txtCn3 = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=FUEL, width=39)
        txtCn3.grid(row=5, column=1)

        lblCn4 = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="*Clothes", padx=2, pady=2, bg="Ghost White")
        lblCn4.grid(row=6, column=0, sticky=W)
        txtCn4 = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=CLOTHES, width=39)
        txtCn4.grid(row=6, column=1)

        lblCn5 = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="*Entertainment", padx=2, pady=2,
                       bg="Ghost White")
        lblCn5.grid(row=7, column=0, sticky=W)
        txtCn5 = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=ENTERTAINMENT, width=39)
        txtCn5.grid(row=7, column=1)

        lblCn6 = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="*Electricity", padx=2, pady=2, bg="Ghost White")
        lblCn6.grid(row=8, column=0, sticky=W)
        txtCn6 = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=ELECTRICITY, width=39)
        txtCn6.grid(row=8, column=1)

        # buttoncall=Button(DataFrameLeft,text="SUM",width=30,height=2,bd=4,fg='white',bg='black',relief=GROOVE,state=DISABLED).grid(row=9,column=0)
        # buttoncall.configure(state=NORMAL)

        # lblAm = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Total Amount:", padx=2, pady=2, bg="Ghost White")
        # lblAm.grid(row=10, column=0, sticky=W)
        txtAm = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=TOTAL_AMOUNT, width=39)
        # txtAm.grid(row=10, column=1)

        # lblDoB = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Date:", padx=2, pady=2, bg="Ghost White")
        # lblDoB.grid(row=3, column=0, sticky=W)
        # txtDoB = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        # txtDoB.grid(row=3, column=1)

        # --------------------------ListBox & ScrollBar-------------
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        categorylist = Listbox(DataFrameRight, width=38, height=15, font=('arial', 12, 'bold'),
                               yscrollcommand=scrollbar.set)
        categorylist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=categorylist.yview)

        # -----------------Button--------------------------------------

        btnAdd = Button(ButtonFrame, text="Add", font=("arial", 20, 'bold'), height=1, width=10, bd=4, command=AddData1)
        btnAdd.grid(row=0, column=0)

        btnSearch = Button(ButtonFrame, text="Search", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                           command=searchData1)
        btnSearch.grid(row=0, column=1)

        btnView = Button(ButtonFrame, text="View", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                         command=viewData1)
        btnView.grid(row=0, column=2)

        # btnEdit= Button(ButtonFrame, text="Edit", font=("arial", 20, 'bold'), height=1, width=10, bd=4,command=update1)
        # btnEdit.grid(row=0, column=3)

        btnDel = Button(ButtonFrame, text="Delete", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                        command=deleteData1)
        btnDel.grid(row=0, column=3)

        btnClear = Button(ButtonFrame, text="Clear", font=("arial", 20, 'bold'), height=1, width=10, bd=4,
                          command=clearData1)
        btnClear.grid(row=0, column=4)

    Button(f2, text="EXPENSES ", font=("Times", "10", "bold italic"), height=5, width=39, fg="White", bg="RED",
           relief=SOLID, command=find).place(x=45, y=200)

    # Button(f2, text="INCOME CATEGORY", font=("Times", "10", "bold italic"), height=5, width=39, fg="White", bg="RED",
    #        relief=SOLID).place(x=45, y=300)


   #--------------------------Expenses pictorial representation----------------------------------------------------------

    usermon = Variable()

    def result():
        Number=Variable()
        Date=Variable()
        Category=Variable()
        Amount=Variable()

        def viewData(date):
            DetailList.delete(0,END)
            for row in budget_backend.viewData(date):
                DetailList.insert(END, row, str(""))



        def action():

            value= comboview.get()
            print(value)
            #for row in budget_backend.showcolumns():
             #DetailList.insert(END,row[0],str(""))
            if(value=="Monthly"):
                label2 = Label(Imf3, text="ENTER MONTH:", height=1, width=25, font=(("Helvetica", 10, "bold italic")))
                label2.place(x=420, y=460)
                month= Entry(Imf3, bd=6, bg="white", width=35, textvariable=usermon).place(x=650, y=455)
                usermon.get()
                btn5 = Button(Imf3, width=10, font=('arial', 10, 'bold'), bg="blue", fg="white",
                             text="Click", command=Click)
                btn5.place(x=500,y=500)

        def Click():
            if(usermon.get()!=0):

                    x1 = pd.DataFrame(budget_backend.barexpcat())
                    y1 = pd.DataFrame(budget_backend.monthd(usermon.get()))
                    a = x1[2:8]
                    print(a)
                    b = y1.T
                    print(b)
                    # labels for bars

                    # plotting a bar chart
                    plt.bar(a[0], b[0])

                    # naming the x-axis
                    plt.xlabel('Category')
                    # naming the y-axis
                    plt.ylabel('Amount')
                    # plot title
                    plt.title('Month Expense(By user)')

                    # function to show the plot
                    plt.show()










        Imf3 = Frame(obj, height=800, width=1900, bg="firebrick4", relief=RAISED).place(x=350, y=95)
        imf3 = Frame(Imf3, bd=2, padx=54, pady=8, bg="tomato", relief=RIDGE)
        imf3.place(x=700,y=100)
        lblim = Label(imf3, font=('arial', 25, 'bold'), text="Result View", bg="Ghost White", fg="black")
        lblim.grid()

        DataFrame = Frame(Imf3, bd=2, width=1900, height=800, padx=20, pady=30, relief=RIDGE, bg="red1")
        DataFrame.place(x=650,y=200)
        viewresult=ttk.Label(DataFrame,font=('arial',20,'bold'),text="Select view type")
        viewresult.pack()

        DataFrame1 = Frame(Imf3, bd=4, width=1500, height=700, padx=20, pady=20, relief=RIDGE, bg="white")
        DataFrame1.place(x=380,y=350)



        lblDate = Label(DataFrame, font=('arial', 13, 'bold'), text="Date:", padx=2, pady=2, bg="red1")
        # lblDate.grid(row=0, column=2, sticky=W)
        txtDate = Entry(DataFrame, font=('arial', 20, 'bold'), textvariable=Date, width=10)
        # txtDate.grid(row=1, column=2)

        comboview=ttk.Combobox(DataFrame,width=70,height=80,font=('arial',10,'bold'),state='readonly')
        comboview.pack()
        comboview.focus()
        comboview['values']=("Daily","Weekly","Monthly")
        #comboview.current(0)
        comboview.set("select")

        btn=Button(DataFrame,width=10,font=('arial',10,'bold'),bg="firebrick4",fg="white",text="submit",command=action)
        btn.pack()

        # --------------------------ListBox & ScrollBar-------------
        scrollbar = Scrollbar(DataFrame1)
        scrollbar.place()
        #scrollbar.grid(row=0, column=1, sticky='ns')

        DetailList = Listbox(DataFrame1, width=120, height=18,bg="firebrick4",fg="white", font=('arial', 12, 'bold'),
                               yscrollcommand=scrollbar.set)
        #categorylist.bind('<<ListboxSelect>>', IncomeRec)
        DetailList.grid(row=0, column=0)
        scrollbar.config(command=DetailList.yview)


    Button(f2, text="Pictorial Representation ", font=("Times", "10", "bold italic"), height=5, width=39, fg="White", bg="RED",
           relief=SOLID,command=result).place(x=45, y=300)






#................................Dashboard...................................


    def result():
        total_exp = StringVar()
        total_inc = StringVar()
        balance= StringVar()

        def viewData(date):
            DetailList.delete(0, END)
            for row in budget_backend.viewData(date):
                DetailList.insert(END, row, str(""))

        def action():
            value =Combobox.get()
            print(value)
            for row in budget_backend.showcolumns():
                DetailList.insert(END, row[0], str(""))
            # if(value=="Daily"):
            #     #DetailList.delete(0, END)
            #     for row in budget_backend.viewData():
            #         DetailList.insert(END, row, str(""))


        def bargraph1():

            x1=pd.DataFrame(budget_backend.barinccat())
            y1=pd.DataFrame(budget_backend.barincamt())
            print(x1)
            print(y1)

            height = [10, 24, 36, 40, 5]

            # labels for bars
            tick_label = ['one', 'two', 'three', 'four', 'five']

            # plotting a bar chart
           # plt.bar(x1[0], y1[0])
            colors = ['b', 'g', 'r', 'c', 'm', 'y']
            #explode = (0.2, 0, 0,0)
            plt.pie(y1[0], colors=colors, labels=x1[0], autopct='%1.1f%%',
                    counterclock=False)

           # naming the x-axis
            #plt.xlabel('Category')
            # naming the y-axis
            #plt.ylabel('Amount')
            # plot title
            plt.title('Total Income(till now)')

            # function to show the plot
            plt.show()


        def bargraph2():

            x1 = pd.DataFrame(budget_backend.barexpcat())
            y1 = pd.DataFrame(budget_backend.barexpcamt())
            a=x1[2:8]
            print(a)
            b=y1.T
            print(b)
            # labels for bars


            # plotting a bar chart
            plt.bar(a[0], b[0])

            # naming the x-axis
            plt.xlabel('Category')
            # naming the y-axis
            plt.ylabel('Amount')
            # plot title
            plt.title('Total Expense(Category wise)')

            # function to show the plot
            plt.show()











        Imf3 = Frame(obj, height=800, width=1900, bg="firebrick4", relief=RAISED).place(x=350, y=95)
        imf3 = Frame(Imf3, bd=2, padx=54, pady=8, bg="tomato", relief=RIDGE)
        imf3.place(x=700,y=100)
        lblim = Label(imf3, font=('arial', 25, 'bold'), text="DASHBOARD", bg="white", fg="black")
        lblim.grid()

        DataFrame = Frame(Imf3, bd=2, width=1500, height=800, padx=20, pady=30, relief=RIDGE, bg="tomato")
        DataFrame.place(x=380,y=200)
        # viewresult = ttk.Label(DataFrame, font=('arial', 20, 'bold'), text="Select view type")
        # viewresult.pack()

        DataFrame1 = Frame(Imf3, bd=4, width=1500, height=700, padx=20, pady=20, relief=RIDGE, bg="white")
        DataFrame1.place(x=380, y=350)



        lbltotalInc = Label(DataFrame, font=('arial', 20, 'bold'), text="Total Income", padx=2, pady=2, bg="Ghost White",relief=GROOVE)
        lbltotalInc.grid(row=0, column=0, padx=9,pady=10)
        txttotalInc= Entry(DataFrame, font=('arial', 20, 'bold'), textvariable=total_inc,state='readonly',width=10)
        txttotalInc.grid(row=1, column=0,padx=9,pady=10)
        total_inc.set(budget_backend.total_income())


        lbltotalExp = Label(DataFrame, font=('arial', 20, 'bold'), text="Total Expense", padx=2, pady=2, bg="Ghost White",
                        relief=GROOVE)
        lbltotalExp.grid(row=0, column=5, padx=9,pady=10)
        txttotalexp = Entry(DataFrame, font=('arial', 20, 'bold'), textvariable=total_exp, state='readonly', width=10)
        txttotalexp.grid(row=1, column=5,padx=9,pady=10)
        total_exp.set(budget_backend.total_exp())

        lblBal = Label(DataFrame, font=('arial', 20, 'bold'), text="Balance", padx=2, pady=2, bg="Ghost White",
                        relief=GROOVE)
        lblBal.grid(row=0, column=9, padx=10,pady=10)
        txtBal = Entry(DataFrame, font=('arial', 20, 'bold'), textvariable=balance, state='readonly', width=10)
        txtBal.grid(row=1, column=9,padx=9,pady=10)
        balance.set(budget_backend.balance())

        btn1 = Button(DataFrame, width=20,height=2, font=('arial', 10, 'bold'), text="Pie Chart For Income", command=bargraph1)
        #btn1.place(x=400, y=400)
        btn1.grid(row=1,column=12,padx=9)


        btn2 = Button(DataFrame, width=20,height=2, font=('arial', 10, 'bold'), text="Bar Graph For Expenses", command=bargraph2)
        #btn1.place(x=400, y=400)
        btn2.grid(row=1,column=22,padx=9)

        # comboview = ttk.Combobox(DataFrame, width=70, height=80, font=('arial', 10, 'bold'), state='readonly')
        # comboview.pack()
        # comboview.focus()
        # comboview['values'] = ("Daily", "Weekly", "Monthly")
        # # comboview.current(0)
        # comboview.set("select")

        # btn = Button(DataFrame, width=10, font=('arial', 10, 'bold'), text="submit", command=action)
        # btn.pack()

        # --------------------------ListBox & ScrollBar-------------
        scrollbar = Scrollbar(DataFrame1)
        scrollbar.place()
        # scrollbar.grid(row=0, column=1, sticky='ns')

        DetailList = Listbox(DataFrame1, width=120, height=18, font=('arial', 12, 'bold'),
                             yscrollcommand=scrollbar.set)
        # categorylist.bind('<<ListboxSelect>>', IncomeRec)
        DetailList.grid(row=0, column=0)
        scrollbar.config(command=DetailList.yview)

    Button(f2, text="DASHBOARD ", font=("Times", "10", "bold italic"), height=5, width=39, fg="White", bg="RED",
           relief=SOLID, command=result).place(x=45, y=400)

    obj.mainloop()





def connt2():
    p=str(user.get())
    q=str(pswd.get())
    mdb=ms.connect(user="root",password="pb11ap7110",host="127.0.0.1",database="login")
    cur=mdb.cursor()
    r=cur.execute("SELECT * FROM login_budget where user='%s'" %p + " and password='%s'"%q)
    record=cur.fetchone()
    if record==None:
        tkinter.messagebox.showinfo('info',"Not Connected")
    else:
        tkinter.messagebox.showinfo('info',"LOGIN SUCCESSFUL")
        obj.destroy()

        obj2()

user=StringVar()
pswd=StringVar()

obj.geometry("1920x1080")
obj.title("BUDGET")
obj.configure(background="white")
photo5 = PhotoImage(file="my2.png")
label = Label(obj, image=photo5)
label.place(x=5, y=1)
Tops=Frame(obj,width=1920,height=90,bg="black",bd=14,relief=GROOVE)
Tops.pack(side=TOP)
lb1title=Label(Tops,text="HOME BUDGET",bg="purple",fg="blue4",justify="center",padx=200,font=("Times 16 bold",25,"italic"))
lb1title.pack()

label1=Label(obj,text="ENTER USERNAME:",height=1,width=25,font=(("Helvetica", 10, "bold italic")))
label1.place(x=520,y=260)
entry=Entry(obj,bd=6,bg="white",width=35,textvariable=user,fg="black").place(x=750,y=255)
label2=Label(obj,text="ENTER PASSWORD:",height=1,width=25,font=(("Helvetica", 10, "bold italic")))
label2.place(x=520,y=340)
entry=Entry(obj,bd=6,bg="white",textvariable=pswd,width=35,show="*",fg="black").place(x=755,y=335)

button=Button(obj,text="LOGIN",bd=6,command=connt2,height=2,width=25).place(x=670,y=400)

obj.mainloop()



