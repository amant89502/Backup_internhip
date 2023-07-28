import sqlite3
connection = sqlite3.connect("myTable.db")
crsr = connection.cursor()
#sql_command = " create table emp(staff_number integer primary key,fname varchar(20),lname varchar(20),gender char(1),birthdate date);"
#crsr.execute(sql_command)
#sql_command1 = """insert into emp values (30,"aman","tiwari","m","2000-06-09");"""
#crsr.execute(sql_command1)
#sql_command2 = """insert into emp values (22,"shubham","sinha","m","2000-02-29");"""
#crsr.execute(sql_command2)
#crsr.execute("update emp set fname='Batak' where staff_number=30");
#crsr.execute("select * from emp where fname='Batak'")
crsr.execute("delete from emp where fname='shubham'")
crsr.execute("select * from emp")
ans = crsr.fetchall()
print(ans)
print("Total changes till now", connection.total_changes)

connection.commit()
connection.close()
