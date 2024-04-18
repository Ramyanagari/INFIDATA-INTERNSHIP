def charge_library():
    days=int(input("enter the no.of days:"))
    if(days<=5):
        charge=days*2
        print("charge is:",charge)
    elif(days>=6 and days<=10):
        charge=days*3
        print("charge is:",charge)
    elif(days>=11 and days<=15):
        charge=days*4
        print("charge is:",charge)
    else:
        charge=days*5
        print("charge is:",charge)
charge_library()