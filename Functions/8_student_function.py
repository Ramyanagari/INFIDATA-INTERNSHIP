def read():
    global name,id,email,test1,test2,test3
    name=input("enter the name")
    id =int(input("enter the id"))
    email = input("enter the email")
    test1 =float(input("enter the test1"))
    test2=float(input("enter the test2"))
    test3 =float(input("enter the test3"))

def display():
       avg=test1+test2+test3/3
       print("student name is:",name)
       print("student id is:",id)
       print("student email is:",email)
       print("student test1 is:",test1)
       print("student test2 is:",test2)
       print("student test3 is:",test3)
       print("Test Avearge marks is:",avg)

print("student details")
read()
display()