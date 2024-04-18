a=int(input("enter total working days"))
b=int(input("enter total absent days"))
c=(a-b)/a
if(c<=75):
    print("student will be not able to take the exams")
else:
    print("student will be able to take the exams")