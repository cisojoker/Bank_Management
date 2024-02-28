import os
import platform
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host="localhost", \
                               user="root", \
                               password="", \
                               database="bank")
mycursor = mydb.cursor()


def AccInsert():
    L = []
    Accno = int(input("Enter the account number : "))
    L.append(Accno)
    name = input("Enter the Customer Name: ")
    L.append(name)
    age = int(input("Enter Age of Customer : "))
    L.append(age)
    occup = input("Enter the Customer Occupation : ")
    L.append(occup)
    Address = input("Enter the Address of the Customer : ")
    L.append(Address)
    Mob = int(input("Enter the Mobile number : "))
    L.append(Mob)
    aadhaarno = int(input("Enter the Aadhaar number : "))
    L.append(aadhaarno)
    Amt = float(input("Enter the Money Deposited : "))
    L.append(Amt)
    AccType = input("Enter the account Type (Saving/RD/PPF/Current) : ")
    L.append(AccType)
    cust = (L)
    sql = '''Insert into account(accno,name,age,occupation,address,mobile,aadhaarno,balance,acctype)
          values(%s,%s,%s, %s,%s,%s, %s,%s,%s)'''
    mycursor.execute(sql, cust)
    mydb.commit()


def AccView():
    print("Select the search criteria : ")
    print("1. Acc no")
    print("2. Name")
    print("3. Mobile")
    print("4. Aadhaar")
    print("5. View All")
    ch = int(input("Enter the choice : "))
    if ch == 1:
        s = int(input("Enter ACC no : "))
        sql = 'select * from account where accno like "%' + str(s) + '%"'
        # print(sql)
        mycursor.execute(sql)
    elif ch == 2:
        s = input("Enter Name : ")
        # rl=(s,)
        sql = 'select * from account where name like "%' + s + '%"'
        # print(sql)
        mycursor.execute(sql)
    elif ch == 3:
        s = int(input("Enter Mobile No : "))
        rl = (s,)
        sql = "select * from account where mobile=%s"
        mycursor.execute(sql, rl)
    elif ch == 4:
        s = input("Enter Aadhaar : ")
        rl = (s,)
        sql = "select * from account where aadhaarno=%s"
        mycursor.execute(sql, rl)
    elif ch == 5:
        sql = "select * from account"
        mycursor.execute(sql)
    columns = []
    res = mycursor.fetchall()
    print("The Customer details are as follows : ")
    k = pd.DataFrame(res)
    if len(k):
        k.columns = ["Id",'Acc no', 'Name', 'Age', 'Occupation', 'Address', 'Mobile', 'Aadhaar', 'Balance', 'Acc Type']
        k.set_index("Acc no")
        k2=k.drop(columns=["Id","Address","Mobile","Aadhaar","Occupation"])
        print(k2)
        viewall = int(input("Press 1 for all details, 0 to go back: "))
        if viewall==1:
            # k=k.T
            print(k.T)
    else:
        print("No such record found")


