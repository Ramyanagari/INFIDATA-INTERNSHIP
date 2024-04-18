ch=int(input("select food categorey 1:veg,2:non-veg"))
if(ch==1):
    ch=int(input("select your food 1:Dosa, 2:Rice bath"))
    if(ch==1):
        print("you have ordered Dosa...")
    elif(ch==2):
        print("you have ordered Rice bath..")
    else:
        print("invalid choice")
elif(ch==2):
    print("you have selected non-veg Dish")
else:
    print("invalid choice")
