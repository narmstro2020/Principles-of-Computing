#You are to create a guess the number game.  
from random import randint

secret_number = randint(0, 20)

user_guess = input("Enter a guess between 0 and 20")
user_guess_num = int(user_guess)
number_of_guesses = 1
while user_guess != secret_number:
    number_of_guesses += 1
    #print some message that says you guessed wrong.  
    #ask the user again to enter a guess and store in user_guess

print("Good job. The answer was", secret_number)
print("Good job. It took you", number_of_guesses, "tries")