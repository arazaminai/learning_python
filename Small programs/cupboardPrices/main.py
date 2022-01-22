from art import start_up
import math


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


def calculator(wood, length, height, depth):
    wood_price = {"mdf": 500, "sunta": 400}
    wood_standard = wood_price[wood.lower()]/1.83/3.66
    our_price = (wood_standard * 10)/(0.7 * 0.5)

    box_price = our_price * length * height * depth

    shelp_price = wood_standard + wood_standard*0.3
    shelp_price *= depth * length

    final_price = roundup(box_price + shelp_price)
    print(f"{final_price}₺")


print(start_up)
wood = input("Sunta or MDF?: ")
while not(wood.lower() == "sunta" or wood.lower() == "mdf"):
    wood = input("Sunta or MDF?: ")

while True:
    try:
        lenght = float(input("lenght in cm: "))/100
        height = float(input("Height in cm: "))/100
        depth = float(input("Depth in cm: "))/100
        break
    except ValueError:
        continue
calculator(wood, lenght, height, depth)