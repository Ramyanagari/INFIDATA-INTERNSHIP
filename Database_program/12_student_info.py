import mysql.connector


#create the connection object
myconn=mysql.connector.connect(
    host="localhost",user="root",password="",database="college")

#creating the cursur cbject
cur=myconn.cursor()


try:
    cur.execute("create table studentinfo(f_name varchar(20),l_name varchar(30),email varchar(20),gender varchar(10),age int(10),bday varchar(20),address varchar(30))")
    print("your table is created successfully")


except Exception as e:
    #myconn.rollback()
    print("can not process:",e)


myconn.close()
