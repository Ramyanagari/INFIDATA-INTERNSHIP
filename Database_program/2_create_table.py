import mysql.connector

#create the connection object
myconn = mysql.connector.connect(
    host="localhost",user="root",passwd="",database="company")

#creating the cursor object
cur = myconn.cursor()

try:
    cur.execute("create table employee(ename varchar(30), eid int(4)primary key,dept varchar(20),designation varchar(20),mobile varchar(10),email varchar(20),place varchar(15))")
    print("your table is created successfully")

except Exception as e:
    #myconn.rollback()
    print("can not process",e)

myconn.close()