mobileNum = input("Enter the Mobile number : ")

def askMobileNumber() :
    global mobileNum
    mobileNum = input("\nPlease enter a valid Mobile number : ")
    validateMobileNumber()
    
def validateMobileNumber() :
    if mobileNum.isdigit() :
        if len(mobileNum) == 10 :
            print("\nYou have entered valid Mobile number. Thank you")
        else :
            askMobileNumber()
    else :
        askMobileNumber()

validateMobileNumber()
