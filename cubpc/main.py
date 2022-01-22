from art import start_up
import math


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


def calculator(wood, length, height, depth, shelfs):
    wood_price = {"mdf": 500, "sunta": 400}
    wood_standard = wood_price[wood.lower()]/1.83/3.66
    our_price = (wood_standard * 10)/(0.7 * 0.5)

    box_price = our_price * length * height * depth

    shelp_price = wood_standard * 1.3
    shelp_price *= shelfs * (depth * length)

    final_price = roundup(box_price + shelp_price)
    return final_price


print(start_up)

while True:
    while True:
        try:
            lenght = float(input("lenght in cm: "))/100
            height = float(input("Height in cm: "))/100
            depth = float(input("Depth in cm: "))/100
            shelfs = int(input("How many full shelfs?: "))
            break
        except ValueError:
            continue
        
    
    wood_types = ["sunta", "mdf"]
    for i in range(len(wood_types)):
        price = calculator(wood_types[i], lenght, height, depth, shelfs)
        print(f"{wood_types[i].title()}: {price}₺")
    print("\n")