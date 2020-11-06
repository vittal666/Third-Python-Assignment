word = input("Enter a string : ")

lowerCaseCount = 0
upperCaseCount = 0

for char in word:
    print(char)
    if char.islower() :
        lowerCaseCount = lowerCaseCount+1
    if char.isupper() :
        upperCaseCount = upperCaseCount+1
        
print("Number of Uppercase characters in the string is :", lowerCaseCount)
print("Number of Lowercase characters in the string is :", upperCaseCount)
