import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",user="root",password="",database="company")

cur=myconn.cursor()

try:
    cur.execute("select * from employee")
    result=cur.fetchall()
    print(result)
except Exception as e:
    print("can not process:",e)
