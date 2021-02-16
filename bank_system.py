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
    
    

def balance_enquiry():
    cur.execute("SELECT * FROM bank;")
    print(cur.fetchall())

def option_chooser(option):
    switcher={
        1: open_account(),
        2: balance_enquiry(),
        7: 0,
    }
    return switcher.get(option, "Option Not Available")
    
    
cur.execute("CREATE TABLE bank (account serial PRIMARY KEY, firstname varchar(20), lastname varchar(20), balance int);")


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
    result = option_chooser(option)        

conn.commit()
cur.close()
conn.close()