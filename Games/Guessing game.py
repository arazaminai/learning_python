secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        break

if out_of_guesses == True:
    print("You Lose")
else:
    print("Congratulations!!! YOU WON!!!")