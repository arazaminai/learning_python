import random, sys

message = ["It is certain",
           "It is decidedly so",
           "Yes definitely",
           "Reply hazy try again",
           "Ask again later",
           "Concentrate and ask again",
           "My reply is no",
           "Outlook not so good",
           "Very doubtful"]

while True:
    print("Ask your question:")
    quetion = input()
    if quetion == "":
        sys.exit()
    print(random.choice(message))