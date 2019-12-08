import random

secret_number = random.randint(1,20)
print("I'm thinking of a number between 1 & 20")

for guesses in range(1, 7):
    print("Take a guess")
    guess = int(input())
    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        break

if guess == secret_number:
    print("Good job! You guessed my number in " + str(guesses) + " guesses!")
else:
    print("Nope, my number was " + str(secret_number))