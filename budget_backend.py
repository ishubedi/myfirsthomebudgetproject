import  string
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
cur=mydb.cursor()
#cur.execute("CREATE DATABASE  IF NOT EXISTS Home_Budget")
# cur.execute("CREATE TABLE IF NOT EXISTS Income(id INT NOT NULL AUTO_INCREMENT ,date date,name text,amount INT,PRIMARY KEY(id))")

def incomeData():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Income(cid INT NOT NULL AUTO_INCREMENT ,date date,catname VARCHAR(255),catamount INT,PRIMARY KEY(id))")
    mydb.commit()
    mydb.close()

def addIncCat(cid,date,catname,catamount ) :
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur = mydb.cursor()
    #cur.execute(" Income VALUES (NULL,?,?,?)",cid,date,catname,catamount)
    cur.execute(' INSERT INTO Income VALUES (%s,%s,%s,%s)',(cid,date, catname, catamount))

    mydb.commit()
    mydb.close()

def viewIncData():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT * FROM Income")
    rows=cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def deleteIncData(cid):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur=mydb.cursor()
    cur.execute("Delete FROM Income where cid=%s",(cid,))
    mydb.commit()
    mydb.close()

def searchIncData(cid="",date="",catname="",catamount=""):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT * FROM Income where cid=%s OR date=%s OR catname=%s OR catamount=%s ",(cid,date,catname,catamount))
    rows = cur.fetchall()
    mydb.close()
    return rows

def dataUpdate(cid,date="",catname="",catamount=""):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("UPDATE Income SET  date=%s,catname=%s , catamount=%s ,where cid=%s", (date,catname,catamount,cid))
    mydb.commit()
    mydb.close()


#--------------------------------------Expense-----------------------------------------------------#

#import mysql.connector
#mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
#cur=mydb.cursor()
#cur.execute("CREATE DATABASE  IF NOT EXISTS Home_Budget")
cur.execute("CREATE TABLE IF NOT EXISTS Expenses(ExTd INT NOT NULL AUTO_INCREMENT ,date DATE,grocery INT(10),medicines INT(10),fuel INT(10),clothes INT(10),entertainment INT(10),electricity INT(10),total_amount FLOAT(10),PRIMARY KEY(ExTd))")

def expensesData():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Expenses(date DATE,grocery INT(10),medicines INT(10),fuel INT(10),clothes INT(10),entertainment INT(10),electricity INT(10),total_amount FLOAT(10))")
    mydb.close()

def addExpCat(ExTd,date,grocery,medicines,fuel,clothes,entertainment,electricity,total_amount ) :
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur = mydb.cursor()
    #cur.execute(" Income VALUES (NULL,?,?,?)",date,grocery,medicines,fuel,clothes,entertainment,electricity )
    cur.execute(' INSERT INTO Expenses VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(ExTd,date,grocery,medicines,fuel,clothes,entertainment,electricity,total_amount))
    mydb.commit()
    mydb.close()

def viewExpData():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT * FROM Expenses ")
    rows=cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows
def totalDateExpData(date):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT grocery,medicines,fuel,clothes,entertainment,electricity ,(grocery+medicines + fuel+clothes+entertainment+electricity)  FROM Expenses where date=%s",(date))
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows
def totalExpData():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT grocery,medicines,fuel,clothes,entertainment,electricity ,(grocery+medicines + fuel+clothes+entertainment+electricity) as 'Total' FROM Expenses")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows


def deleteExpData(date):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="Home_Budget")
    cur=mydb.cursor()
    cur.execute("Delete FROM Expenses where date=%s",(date,))
    mydb.commit()
    mydb.close()




def lastId():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    lastId=cur.lastrowid
    mydb.commit()
    mydb.close()
    return lastId

def searchExpData(date=''):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT * FROM Expenses where date=%s",(date,))
    rows = cur.fetchall()
    mydb.close()
    return rows

def viewData():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("Select date as Date,grocery as Grocery ,medicines as Medicines,fuel as Fuel,clothes as Clothes,entertainment as Entertainment,electricity as Elec_Bills,total_amount as Total_Expense from expenses where date='2019-05-06'")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def showcolumns():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE  table_name = 'expenses'    AND table_schema = 'home_budget'")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows


def total_income():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT sum(catamount) FROM income ")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def total_exp():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT sum(total_amount) FROM expenses   ")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def balance():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT (sum(catamount)- (SELECT sum(total_amount) FROM expenses) )FROM   income   ")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows


def barinccat():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("select catname  from income group by catname ")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def barincamt():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("select sum(catamount) from income group by catname ")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def barexpcat():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE  table_name = 'expenses'    AND table_schema = 'home_budget'")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def barexpcamt():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT sum(grocery),sum(medicines),sum(fuel),sum(clothes),sum(entertainment),sum(electricity)  FROM Expenses ")
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows

def monthd(mon):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="Home_Budget")
    cur = mydb.cursor()
    cur.execute("SELECT sum(grocery),sum(medicines),sum(fuel),sum(clothes),sum(entertainment),sum(electricity) FROM expenses WHERE month (date)= %s group by month(date)",(mon,))
    rows = cur.fetchall()
    mydb.commit()
    mydb.close()
    return rows
