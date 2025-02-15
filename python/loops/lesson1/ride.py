print("select your ride")
print("1.bike")
print("2.car")

choice = int(input("enter your choice"))

if (choice==1):
    print("what type of bike")
    print("1.scooty\n")
    print("2.scooter\n")

    choice2 = int(input("enter your second choice"))
    if choice2 == 1:
        print("ypu have seleceted scooty")
    else:
        print("you have selected scooter")

elif(choice==2):
    print("what type of car")
    print("1.seden\n")
    print("2.xuv\n")
    choice3 = int(input("enter yoiur choice"))
    if choice3 == 1:
        print("you have selected seden")
    else:
        print("you have selected xuv")
else:
    print("wrong choice")


