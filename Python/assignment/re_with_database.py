import re
import sqlite3


def ver_name(name):
    pattern_name = re.compile('[a-z | A-Z]+$')
    if pattern_name.match(name):
        return True
    else:
        return False


def ver_mobile(mobile):
    pattern_mobile=re.compile('([0-9]{10}$)')
    if pattern_mobile.match(mobile):
        return True
    else:
        return False


def ver_email(email):
    pattern_email = re.compile('^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')
    if pattern_email.match(email):
        return True
    else:
        return False


connection = sqlite3.connect("PageUI.db")
crsr = connection.cursor()
"""query = "create table login (id integer primary key,name varchar(30),phone int,email varchar(25),passwd varchar(30))"
#crsr.execute(query)
"""


def new_registration():

    id = input("Enter your ID")
    name = input("Enter Your Name")
    phone = input("Enter your phone number")
    email = input("Enter your email id")
    password = input("Enter your password")
    details = [id, name, phone, email, password]
    crsr.execute("insert into login values (?,?,?,?,?)", details)
    connection.commit()

#new_registration()


def login():
    em = input("Enter your email")
    password = input("Enter your password")
    crsr.execute("select name from login where passwd=(?);", [password])
    b = crsr.fetchall()
    print(b)


def change_details():
    print("Changing the data")
    print("Enter \n1.For changing name\n2.For changing phone\n3.For changing email\n4.For changing password")


a = 0
while a != 4:
    a = int(input("Enter your choice \n1.Registration\n2.login"))
    if a == 1:
        new_registration()
    elif a == 2:
        login()










