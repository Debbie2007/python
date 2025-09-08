"""
Guess the Number:
Set a secret number (e.g., 7) and Ask the user to guess the number.
Keep asking until they guess correctly
When guessed right, print "Correct! You win."
"""
secret_number = 5
guess = None

while guess != secret_number:
    guess = int(input("Guess the number:"))
    if guess == secret_number:
        print("correct! you win")
    else:
       print("wrong! Try again.")