age=int(input("enter your age:"))
if(age>=18 and age<30):
    gender=input("enter your gender m/f")
    if(gender=='m'):
        days=int(input("enter no.of.days"))
        wages=700*days
        print("wages is:",wages)
    elif(gender=='f'):
        days=int(input("enter n0.of days"))
        wages=750*days
        print("wages is:",wages)
    else:
        print("invalid choice")
elif(age>=30 and age<=40):
    gender = input("enter your gender m/f")
    if (gender == 'm'):
        days = int(input("enter no.of.days"))
        wages = 800 * days
        print("wages is:", wages)
    elif (gender == 'f'):
        days = int(input("enter n0.of days"))
        wages = 850 * days
        print("wages is:", wages)
    else:
        print("invalid choice")

else:
    print("invalid choice")