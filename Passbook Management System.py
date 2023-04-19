#passbook management system


import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="bank")
cursor=mydatabase.cursor()
# cursor.execute("create database bank")
# cursor=mydatabase.cursor()
# cursor.execute("create table Account_details(name varchar(200),accid int primary key auto_increment,password varchar(8),balance float)")
# cursor.execute("alter table Account_details auto_increment=100000000000");

def createacc():
    query="insert into Account_details(name,password,balance) values(%s,%s,%s)"
    name=input("Enter your FullName = ")
    password=input("Enter 8 digit password to secure your Account = ")
    # password = getpass.getpass(prompt="Enter your password: ", echo=False)
    balance=float(input("Enter Amount you wish to deposit in your account = "))
    mydatabase.cursor()
    cursor.execute(query,[name,password,balance])
    mydatabase.commit()
    acc=f"select accid from Account_details where name='{name}'"
    cursor.execute(acc)
    a=cursor.fetchall()
    for i in a:
        r=i[0]
    print("Congratulations,Your Account is created and your AccountId is",r)
    mydatabase.commit()
    start()
    
def checkbal():
    query1="select password from Account_details where accid = %s "
    accid=int(input("Enter your Accid = "))
    password=input("Enter your password = ")
    cursor.execute(query1,[accid])
    a=cursor.fetchall()
    try:
        if a[0][0]==password:
                query2=f"select balance from Account_details where accid='{accid}' and password='{password}'"
                mydatabase.cursor()
                cursor.execute(query2)    
                b=cursor.fetchall()
                print("Your Account Balance is",b[0][0])
        else:
                print("Please check your password")
        mydatabase.commit()
        start() 
    except Exception:
        print("Invalid credentials, Please enter your Account ID and Password again ")
        start()
def depoamt():
    query=f"select balance from Account_details where accid= %s "
    accid=int(input("Enter your Account ID = "))
    depo=float(input("Enter Amount to Deposit = "))
    cursor.execute(query,[accid])
    a=cursor.fetchall()
    try:
        if type(depo)==type(a[0][0]) and depo>0:
            query2="update Account_details set balance = %s where accid= %s "
            upbal=float(a[0][0]) + depo
            mydatabase.cursor()
            cursor.execute(query2,[upbal,accid])
            mydatabase.commit()
            query3=f"select balance from Account_details where accid='{accid}'"
            cursor.execute(query3)
            a=cursor.fetchall()
            print("Your Updated Balance is : ",a[0][0])
        else:
            print("Please Enter Valid Amount")
        mydatabase.commit()
        start()
    except Exception:
        print("Invalid Account Id")
        start()
    
def withamt():
    accid=int(input("Enter your Account Id = "))
    pas=input("Enter Account password = ")
    query5=f"select password from Account_details where accid='{accid}'"
    cursor.execute(query5)
    b=cursor.fetchall()
    try:
        if b[0][0]==pas:
            query=f"select balance from Account_details where accid='{accid}' and password='{pas}'"
            cursor.execute(query)
            a=cursor.fetchall()
            amt=float(input("Enter Amount which you want to withdraw = "))
            if amt<a[0][0] and amt>0:
                upbal= a[0][0] - amt
                query2=f"update Account_details set balance='{upbal}' where accid='{accid}'"
                cursor.execute(query2)
                mydatabase.commit()
                print(f"Your Account is debited with {amt} & Your updated Balance is {upbal}")
                start()
            else:
                print("Check Entered Amount")
                start()
        else:
            print("Invalid Password, Please try Again")
            start()
    except Exception:
        print("Invalid credentials, Please enter your Account ID and Password again")
        start()

def start():
    print("=============================Menu==================================")
    print("1.Create Account")
    print("2.Check Balance")
    print("3.Deposit an Amount")
    print("4.Withdraw an Account")
    print("0.Exit")
 
    choice = int(input("Enter your choice : "))
    match choice:
        case 1:createacc()
        case 2:checkbal()
        case 3:depoamt()
        case 4:withamt()
        case 0:exit()
        case _:
            print("Invalid Entry,Please try again")
    start()
start()