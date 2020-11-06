input_list = []
n = int(input("Enter the list size : "))
print("\n")

for i in range(0, n):
    print("Enter number", i+1, " : ")
    item = int(input())
    input_list.append(item)
    
print("\nEntered List is : ", input_list)

sampleTuple = ()
unique_list = []

listSize = -1
for i in input_list: 
    if i not in unique_list: 
        listSize+=1
        unique_list.append(i)
            
unique_list.sort()
print("Unique_list is : ", unique_list)

finalTuple = tuple(unique_list)

print("Tuple is : ", finalTuple)

print("Minimum is : ", finalTuple[0])

print("Maximum is : ", finalTuple[listSize])
