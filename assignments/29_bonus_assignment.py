def emp_salary():
    emp_salary=int(input("enter emp_salary:"))
    years_of_service=int(input("enter emp_service:"))

    if years_of_service>10:
        bonus=(10/100)*emp_salary
    elif years_of_service>=6 and years_of_service<=10:
        bonus=(8/100)*emp_salary
    elif years_of_service<6:
        bonus=(5/100)*emp_salary
    print("bonus is:",bonus)
emp_salary()