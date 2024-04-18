emp_salary=int(input("enter emp-salary"))
years_of_service=int(input("enter emp-service"))

if years_of_service>10:
 bonus=(10/100)*emp_salary
if years_of_service>=6 and years_of_service<=10:
   bonus =(8/100)* emp_salary
if years_of_service<6:
    bonus+(5/100)*emp_salary
    print("bonus is:",bonus)