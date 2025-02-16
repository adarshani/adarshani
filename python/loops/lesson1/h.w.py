age = int(input("Enter you age"))

if age<0:
    print("age is invalid")
else:
        if age<18:
            print("you are a minor")
        else:
             if age< 65:
                  print("you are an adult")
             else:
                  print("you are asenior citizen")
    