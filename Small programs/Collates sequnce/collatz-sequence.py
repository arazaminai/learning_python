from collatzrule import collatz

try:
    number = collatz(int(input("Enter number: ")))
    print(number)
except ValueError:
    print("Intergers only")

while number != 1:
    number = collatz(number)
    print(number)
