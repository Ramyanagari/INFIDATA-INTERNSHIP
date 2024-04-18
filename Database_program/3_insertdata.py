import mysql.connector

#Create the connection object
myconn = mysql.connector.connect(
    host="localhost",user="root",passwd="",database="company")

#creating the cursor object
cur = myconn.cursor()

sql = "insert into employee(ename,eid,dept,designation,mobile,email,place) values(%s,%s,%s,%s,%s,%s,%s)"

#The row values are provided in the form of tuple
name=input("enter employee name:")
eid=int(input("enter emp id:"))
dept=input("enter dept name:")
designation=input("enter designation:")
mobile=input("enter mobile num:")
email=input("enter ur email id:")
place=input("enter your work place:")


val = (name,eid,dept,designation,mobile,email,place)

try:
    #inserting the values into the table
    cur.execute(sql,val)
    myconn.commit()   #commit the transaction
    print("data inserted")

except Exception as e:
    print("can not process",e)
    myconn.rollback()

print(cur.rowcount,"record inserted!")
myconn.close()


