lower = int(input("Enter the lower range -"))
upper = int(input('enter the upper range-'))

print("prime nuber between the",lower,"and",upper)
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break

        else:   
            print(num)
