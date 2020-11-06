def outerFunction():
    a = int(input("Enter value for 'a' : "))
    b = int(input("Enter value for 'b' : "))
    
    def innerAdditionFun(num1, num2) :
        return num1 + num2
    
    sum = innerAdditionFun(a, b)
    
    return sum+5

print("Final result is : ", outerFunction())
