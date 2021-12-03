import random 
print('number guessing game')
number=random.randint(1,9)
chances=0
print('guess a number between 1 and 9: ')
while chances < 5:
    guess=int(input('enter your guess number: '))

    if guess == number:
        print('CONGRADULATIONS U WON!!!')
        break
    elif guess < number:
        print('Your guess was too low guess a higher number than',guess)
    else: 
         print('Your guess was too high guess a lower number than',guess)
    chances+=1

if not chances < 5: 
    print('U LOSE!!! THE NUMBER IS ',number)

