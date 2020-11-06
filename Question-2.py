input_list = []
n = int(input("Enter the list size : "))
print("\n")

for i in range(0, n):
    print("Enter number", i+1, " : ")
    item = int(input())
    input_list.append(item)
    
print("\nEntered List is : ", input_list)

freq_dict = {}

for item in input_list: 
    if (item in freq_dict): 
        freq_dict[item] += 1
    else: 
        freq_dict[item] = 1

print("\nPrinting count of each item : ")
for key, value in freq_dict.items():
        print(key, " : ", freq_dict[key], " times")
