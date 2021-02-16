DB_HOST = "localhost"
DB_NAME = "mydb"
DB_USER = "azad"
DB_PASS = "azad@#123"

import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

def open_account():
    print("Enter First Name : ", end='')
    f_name = input()
    
    print("Enter Last Name : ", end='')
    l_name = input()
    
    print("Enter the Minimum Balance : ", end='')
    bal = int(input())
    
    cur.execute("INSERT INTO bank (firstname, lastname, balance) VALUES(%s, %s, %s);", (f_name, l_name, bal))
    conn.commit()
    print("\tCONGRATULATIONS !!!!!!! ACCOUNT IS CREATED")
    

def balance_enquiry():
    
    print("Enter the Account Number : ", end='')
    acc = (input())
    
    cur.execute("SELECT * FROM bank where account = (%s);", (acc))
    print(cur.fetchall())

def deposit_money():
    print("Enter the Account Number : ", end='')
    acc_num = (input())
    
    print("Enter the Balance to Deposit : ", end='')
    bal = int(input())
    
    cur.execute("UPDATE bank SET balance =  balance + (%s) WHERE account = (%s);", (bal, acc_num))
    cur.commit()

def withdraw_money():
    print("Enter the Account Number : ", end='')
    acc_num = (input())
    
    print("Enter the Ammount To Withdraw : ", end='')
    bal = int(input())
    
    cur.execute("SELECT * FROM bank where account = (%s);", (acc_num))
    record = cur.fetchall()
    
    for row in record:
        balance = row[3]
    
    if(bal > balance):
        print("Insufficient Balance !!!!!!")
        print("Total Balance in Account ", balance) 
    
    else:
        cur.execute("UPDATE bank SET balance = balance - (%s) WHERE account = (%s)", (bal, acc_num))

def display_all_records():
    cur.execute("SELECT * FROM bank")
    records = cur.fetchall()
    
    for row in records:
        print("Account Number   : ", row[0])
        print("First Name       : ", row[1])
        print("Last Name        : ", row[2])
        print("Balance          : ", row[3])
        print("\n")
        
def option_chooser(option):
    if(option == 1):
        open_account()
    elif(option == 2):
        balance_enquiry()
    elif(option == 3):
        deposit_money()
    elif(option == 4):
        withdraw_money()
    elif(option == 6):
        display_all_records()
    else:
        print("Option Not Available")
        

print("\t1. To Create New Table")
print("\t2. Insert Into Same Table")
option = int(input())

if option == 1:  
    cur.execute("CREATE TABLE bank (account serial PRIMARY KEY, firstname varchar(20), lastname varchar(20), balance int);")
    conn.commit()


while(1):
    print("**************Bank System**************")
    print("\t\t1. Create an Account")
    print("\t\t2. Balance Enquiry")
    print("\t\t3. Deposit")
    print("\t\t4. Withdraw")
    print("\t\t5. Close an Account")
    print("\t\t6. Show all Accounts")
    print("\t\t7. Quit")
    option = int(input())
    
    if(option == 7):
        print("Thanks !!!!!!!!")
        break
    
    option_chooser(option)      

conn.commit()
cur.close()
conn.close()