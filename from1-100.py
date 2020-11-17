
from random import randint

x = 1
y = 100

client_guess = int(input('Try to guess a char from 1 to 100: \n'))
comp_char = randint(x, y)

while client_guess != comp_char:
    client_guess = int(input('Try to guess one more time: \n'))
    if client_guess < comp_char:
        x = client_guess
        print(f'The char is between {x} and {y}\n')
    else:
        y = client_guess
        print(f'The char is between {x} and {y}\n')
print(f'Cool! The char is {client_guess} You are totally right!')
