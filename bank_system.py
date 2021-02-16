DB_HOST = "localhost"
DB_NAME = "mydb"
DB_USER = "****"
DB_PASS = "*******"

import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

def open_account():
    print("Enter the Account Number : ", end='')
    acc = input()
    
    print("Enter First Name : ", end='')
    f_name = input()
    
    print("Enter Last Name : ", end='')
    l_name = input()
    
    print("Enter the Minimum Balance : ", end='')
    bal = input()
    
    try:
        cur.execute("INSERT INTO bank (account, firstname, lastname, balance) VALUES(%s, %s, %s, %s);", (acc, f_name, l_name, bal))
        conn.commit()
        print("\tCONGRATULATIONS !!!!!!! ACCOUNT IS CREATED")
    
    except Exception as e:
        print("************WARNING************")
        print("\tAccount Number is Already Taken!!!!!!!", e)
        conn.rollback()
    
def balance_enquiry():
    
    print("Enter the Account Number : ", end='')
    acc = (input())
   
    try: 
        cur.execute("SELECT * FROM bank where account = ('%s')" % (acc))
        
        print(acc)
        record = cur.fetchall()
        
        print("************ ACCOUNT HOLDERS DETAIL ************")
        for row in record:
            print("\n")
            print('Account Number     : ', row[0])
            print('First Name         : ', row[1])
            print('Last Name          : ', row[2])
            print('Balance            : ', row[3])

    except Exception as e:
        print("Error : ", e)
    print("\n")

def deposit_money():
    print("Enter the Account Number : ", end='')
    acc_num = (input())
    
    print("Enter the Balance to Deposit : ", end='')
    bal = int(input())
    
    cur.execute("UPDATE bank SET balance =  balance + (%s) WHERE account = (%s);" % (bal, acc_num))
    conn.commit()

def withdraw_money():
    print("Enter the Account Number : ", end='')
    acc_num = (input())
    
    print("Enter the Ammount To Withdraw : ", end='')
    bal = int(input())
    
    try:
        cur.execute("SELECT * FROM bank where account = (%s);" % (acc_num))
        record = cur.fetchall()
        
        print("\n")
        for row in record:
            balance = row[3]
        
        if(bal > balance):
            print("************WARNING************")
            print("Insufficient Balance !!!!!!")
            print("Total Balance in Account ", balance) 
        
        else:
            cur.execute("UPDATE bank SET balance = balance - (%s) WHERE account = (%s)" % (bal, acc_num))

    except Exception:
        print("OOPS!!!!!! , Account is Not Present")
    print("\n")
def delete_account():
    print("Enter the Account Number : ", end='')
    acc = input();
    
    try:
        cur.execute("DELETE FROM bank WHERE account = (%s);" % (acc))
        conn.commit()
        print("*********ACCOUNT IS CLOSED SUCCESSFULLY********")
    
    except Exception:
        print("OOPS !!!! , Account is Not Present")
        
def display_all_records():
    cur.execute("SELECT * FROM bank")
    records = cur.fetchall()
    
    print("************ALL ACCOUNT HOLDERS DETAIL************")
    for row in records:
        print("\n")
        print("Account Number   : ", row[0])
        print("First Name       : ", row[1])
        print("Last Name        : ", row[2])
        print("Balance          : ", row[3])
        
def option_chooser(option):
    if(option == 1):
        open_account()
    elif(option == 2):
        balance_enquiry()
    elif(option == 3):
        deposit_money()
    elif(option == 4):
        withdraw_money()
    elif(option == 5):
        delete_account();
    elif(option == 6):
        display_all_records()
    else:
        print("Option Not Available")
        

print("\t1. To Create New Table")
print("\t2. Insert Into Same Table")
option = int(input())

if option == 1:  
    cur.execute("CREATE TABLE bank (account int PRIMARY KEY, firstname varchar(20), lastname varchar(20), balance int);")
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
