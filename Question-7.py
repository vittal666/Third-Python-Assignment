a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))

def helloFunc(a,b):
    return a+b

renamed_hello_fun = helloFunc

print("sum = ", renamed_hello_fun(2,4))
