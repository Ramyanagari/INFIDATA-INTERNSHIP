name=input("enter employee name")
basic_salary=float(input("enter employee basic salary"))
da=0.4*basic_salary
hra=0.2*basic_salary

print("employee name is:",name)
print("employee basicsalary is:",basic_salary)
print("da of the employee is:",da)
print("hra of the employee is:",hra)

gross_salary=basic_salary+da+hra
print("employee gross_salary is:",gross_salary)