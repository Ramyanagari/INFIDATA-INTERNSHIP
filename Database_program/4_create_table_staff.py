import mysql.connector

#create the connection object
myconn=mysql.connector.connect(
    host="localhost",user="root",password="",database="company"
)

#creating the cursor object
cur=myconn.cursor()

try:
    cur.execute("create table staff(emp_id int(10),f_name varchar(30),l_name varchar(30),j_grade varchar(30),dept_id int(10),salary int(10),j_id varchar(10),dept_name varchar(30),mobile varchar(10),email varchar(30))")
    print("your table is created successfully")

except Exception as e:
    #myconn.rollback()
    print("can not process:",e)

myconn.close()
