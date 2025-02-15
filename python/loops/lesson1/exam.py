medical_cause = input("did you have a medical cause Y or N")
attendence = int(input("Enter your attendence"))

if medical_cause == "Y": 
    print("you are allowed")
else:
    if attendence>=75:
        print("you are allowed")
    else:
        print("you are not allowed")


      