import mysql.connector


#create the connection object
myconn=mysql.connector.connect(
    host="localhost",user="root",password="",database="college")

#creating the cursur cbject
cur=myconn.cursor()


try:
    cur.execute("create table student1(name varchar(30),id int(4) primary key,branch varchar(20),email varchar(20),mobile varchar(10))")
    print("your table is created successfully")


except Exception as e:
    #myconn.rollback()
    print("can not process:",e)


myconn.close()
