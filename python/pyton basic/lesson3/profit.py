cp=float(input("Enter the cost price: "))
sp=float(input("Enter the selling price: "))
if cp<sp:
    print("Profit")
    amount=sp-cp
    print("Profit amount: ",amount)
else:
    print("Loss")
    amount=cp-sp
    print("Loss amount: ",amount)



