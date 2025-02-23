string = input("Enter you word")

char = input("Enter the charecter you want to check in string")

i = 0
count=0

while(i<len(string)):

    if (string[i]==char):
        count=count+1

    i=i+1
print("the total number of times the character is repeted is- ",count)