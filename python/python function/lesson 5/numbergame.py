import random
playing = True
number = str(random.randint(1,9))

print('I will generate a number From 0 to 9,amd you have to guess the number one digit at a time')
print('the game ends when you get one')

while playing:
    guess = input('give me your best guess=')
    if number == guess:
        print('you win the game')
        print("the number was",number)
        break
    else:
        print('your guess was not right ! try again!')
