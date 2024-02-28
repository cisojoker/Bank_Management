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
def AccDeposit():
    L = []
    Accno = int(input("Enter the account number : "))
    L.append(Accno)
    Amtdeposit = eval(input("Enter the Amount to be deposited : "))
    L.append(Amtdeposit)
    month = input("Enter month of Salary : ")
    L.append(month)
    cust = (L)
    sql = "Insert into amount(Accno,Amtdeposit,Month) values(%s,%s,%s)"
    mycursor.execute(sql, cust)
    sql = "UPDATE account SET balance= balance + %s where accno = %s"
    mycursor.execute(sql,[L[1],L[0]])
    mydb.commit()
    print("Amount deposited successfully")
    sql = "select balance from account where accno = %s"
    mycursor.execute(sql,[L[0]])
    res = mycursor.fetchall()
    for x in res:
        print("Updated balance is: ",x)

def AccWithdraw():
    L = []
    Accno = int(input("Enter the account number : "))
    L.append(Accno)
    Amtwithdraw = float(input("Enter the Amount to be withdrawn : "))
    L.append(Amtwithdraw)
    Remark = input("Enter remark for Withdrawal : ")
    L.append(Remark)
    cust = (L)
    sql = "Select * from account where accno = %s and balance> %s"
    mycursor.execute(sql, [L[0],L[1]])
    results= mycursor.fetchone()
    if results==None:
        print("Not enough balance available")
    else:
        # withdrawl can happen because account has sufficient balance
        sql = "Insert into amount(Accno,Amtdeposit,month) values(%s,-%s,%s)"
        mycursor.execute(sql, cust)
        sql = "UPDATE account SET balance= balance - %s where accno = %s"
        mycursor.execute(sql, [L[1], L[0]])
        mydb.commit()
        print("Amount withdrawn successfully")
        sql = "select balance from account where accno = %s"
        mycursor.execute(sql, [L[0]])
        res = mycursor.fetchall()
        for x in res:
            print("Updated balance is: ", x)



def accView():
    print("Please enter the details to view the Money details :")
    Accno = int(input("Enter the account number of the Customer whose amount is to be viewed : "))
    sql = '''Select account.Accno, account.Name,
  account.Age,account.occupation,account.Address,account.mobile,account.aadhaarno,account.balance,account.AccType, sum(amt.Amtdeposit), amt.month from account INNER JOIN amount as amt ON
           account.Accno=amt.Accno and amt.Accno = %s'''
    rl = (Accno,)
    mycursor.execute(sql, rl)
    res = mycursor.fetchall()
    for x in res:
        print(x)


def closeAcc():
    Accno = int(input("Enter the account number of the Customer to be closed : "))
    rl = (Accno,)
    sql = "Delete from amount where Accno=%s"
    mycursor.execute(sql, rl)
    sql = "Delete from account where Accno=%s"
    mycursor.execute(sql, rl)
    mydb.commit()


def MenuSet():
    print("Enter 1 : To Add Customer")
    print("Enter 2 : To View Customer ")
    print("Enter 3 : To Deposit Money ")
    print("Enter 4 : To Withdraw Money ")
    print("Enter 5 : To Close account")
    print("Enter 6 : To View All Customer Details")
    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nError! That's Not A Number")
    else:
        print("\n")
        if (userInput == 1):
            AccInsert()
        elif (userInput == 2):
            AccView()
        elif (userInput == 3):
            AccDeposit()
        elif (userInput == 4):
            AccWithdraw()
        elif (userInput == 5):
            closeAcc()
        elif (userInput == 6):
            accView()
        else:
            print("Enter correct choice. . . ")
            MenuSet()


def runAgain():
    runAgn = input("\nWant To Run Again Y/n: ")
    while (runAgn.lower() == 'y'):
        if (platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
MenuSet()
runAgain()
