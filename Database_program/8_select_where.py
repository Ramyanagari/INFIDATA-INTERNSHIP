import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",user="root",password="",database="company")

cur=myconn.cursor()

try:
    cur.execute("select * from employee where eid=102")
    result=cur.fetchall()
    for i in result:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])
except Exception as e:
    print("can not process:", e)