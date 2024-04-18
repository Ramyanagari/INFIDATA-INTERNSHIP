import mysql.connector

#Create the connection object
myconn = mysql.connector.connect(
    host="localhost",user="root",passwd="",database="company")

#creating the cursor object
cur = myconn.cursor()

sql = "insert into staff(emp_id,f_name,l_name,j_grade,dept_id,salary,j_id,dept_name,mobile,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#The row values are provided in the form of tuple
emp_id=int(input("enter employee id:"))
f_name=input("enter emp first name:")
l_name=input("enter emp last name:")
j_grade=input("enter emp job grade:")
dept_id=int(input("enter emp department id:"))
salary=int(input("enter emp salary:"))
j_id=input("enter emp job id:")
dept_name=input("enter emp department name:")
mobile=input("enter emp mobile num:")
email=input("enter emp email id:")

val = (emp_id,f_name,l_name,j_grade,dept_id,salary,j_id,dept_name,mobile,email)

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


