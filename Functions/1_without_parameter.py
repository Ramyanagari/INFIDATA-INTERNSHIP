print("Addition program using function")
#function defination
def addition():
    n1=int(input("enter 1st int num:"))
    n2=int(input("enter 2nd int num:"))
    res=n1+n2
    print("add of {0} and {1} is {2}".format(n1,n2,res))

print("function without parameter Demo")
#calling a function
addition()
print("end of the program")