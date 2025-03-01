print("Enter a charecter", end="")
c = input()

if len(c)>1:
    print("n\Invalid Input!")
else:
    if c>='a'and c<='z':
        print("\n\""+c+"\"Is an Alphabet")
    elif c>='A' and c<='Z':
        print("\n\""+c+"\"Is an Alphabet")
    else:
        print("\n\""+c+"\"Is not an Alphabet")

