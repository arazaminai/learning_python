import art


menu = {
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 10
        },
        "cost": 1.5
    },
    "latte":{
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3
    }
}


resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }


def enough_resouces(order_ingridient):
    for item in order_ingridient:
        if order_ingridient[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True


def inserted_coins():
    print("insert coins...")
    total = 0
    try:
        total = int(input("How many Quaters do you put: ")) * 0.25
        total += int(input("How many Dimes do you put: ")) * 0.1
        total += int(input("How many Nickles do you put: ")) * 0.05
        total += int(input("How many Pennies do you put: ")) * 0.1
    except ValueError:
        total = total
    return total


def transaction(coins, item_cost):
    if coins < item_cost:
        print("sorry, that is not enough money. Money refunded")
        return False
    elif coins >  item_cost:
        change = coins - item_cost
        print(f"Here is ${change} change")
    resources["money"] += item_cost
    return True


def make_coffee(order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]


print(f"{art.start_up}\nWelcome to the coffee machine")
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        print("Shutting down...")
        break
    elif choice == "report":
        print(f"""
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        cofffee: {resources["coffee"]}
        Money: {resources["money"]}
        """)
    else:
        try:
            item = menu[choice]
            ingredients = item["ingredients"]
            if enough_resouces(ingredients):
                print(f"{choice} will be ${item['cost']}")
                if transaction(inserted_coins(), item["cost"]):
                    make_coffee(ingredients)
        except KeyError:
            print("Sorry, drink does not excist.")
                

    

    
