import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",user="root",password="",database="company")

cur=myconn.cursor()

try:
    result=cur.execute("select salary<30000 from staff")
    result=cur.fetchall()
    for i in result:
        print(i)
except Exception as e:
    print("can not process:", e)