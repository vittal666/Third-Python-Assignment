name = input("Enter employee name : ")
salary = input("Enter salary : ")


def showEmployee(eNmae, eSalary=50000):
    print("\nEmployee", eNmae, "salary is :", eSalary)

if salary != "" :
    showEmployee(name, salary)
else :
    showEmployee(name)
