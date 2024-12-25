import random
secret_num = random.randint(1,10)
guess = int(input("Make a guess between 1-10:"))

if (secret_num == guess):
    print("Congratulations, you guessed the secret number!")
elif (guess < secret_num):
    print ('Too low!')
else:
    print ('Too high!')