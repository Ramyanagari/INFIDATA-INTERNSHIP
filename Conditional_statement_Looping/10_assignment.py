cname=input("enter customer name")
cid=int(input("enter customer id"))
units=int(input("enter no_of_units"))

if(units<=100):
    charge=units*0
    print("charge is:",charge)
elif(units>=100 and units<=200):
    charge=(units-100)*5
    print("electricity charge is:",charge)
elif(units>=200):
    charge=(units - 100)*10
    print("electricity charge is:",charge)