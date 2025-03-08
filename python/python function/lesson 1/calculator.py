def add(P,Q):
    return P+Q

def subract(P,Q):
    return P-Q

def multiply(P,Q):
    return P*Q

def dvision(P,Q):
    return P/Q

print("please select the operation")
print("a.add")
print("b.subract")
print("c.multiply")
print("d.division")

choice = input("plese enter your choice a/b/c/d-")

num1 = int(input(" enter the first number"))
num2 = int(input("enter you second number"))

if choice == "a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice== "b":
    print(num1,"-",num2,"=",subract(num1,num2))
elif choice == "c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == "d":
    print(num1,"/",num2,"=",dvision(num1,num2))
else:
    print("not a valid input")



   



