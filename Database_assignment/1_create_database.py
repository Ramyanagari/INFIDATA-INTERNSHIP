import mysql.connector
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = myconn.cursor()


try:

    mycursor.execute("CREATE DATABASE employee")
    print("database created successfully")
except Exception as e:
    print("can not process:",e)

myconn.close()
