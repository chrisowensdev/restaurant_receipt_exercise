menu = {
    "Brunch": {
        "Steak and Eggs": 16.99,
        "Three Egg Breakfast": 8.99,
        "Eggs Benedict": 11.99,
        "Biscuit and Gravy": 7.99,
        "Chicken Fingers": 10.99,
        "Chicken Wrap": 8.99,
        "Steak Salad": 1.99
    },
    "Drinks": {
        "Soft Drink": 1.99,
        "Coffee": 1.99,
        "Orange Juice": 0.99,
        "Milk": 0.55,
        "Water": 0.00
    }
}

# 1. Fix price of Steak Salad to 15.99
menu["Brunch"]["Steak Salad"] = 15.99

# 2. Add Specials Menu
menu["Specials"] = {
    "Soup of the Day": 8.99,
    "Catch of the Day": 14.99,
    "Chef Special": 15.99
}

# 3. Change "Three egg breakfast" options
menu["Brunch"]["Three Egg Breakfast"] = {
    "Without Bacon": 8.99,
    "With Bacon": 9.99
}


def get_item_price(ordered_item):
    for category in menu:
        for item in menu[category]:
            if ordered_item == item:
                return menu[category][item]


def get_receipt(table):
    price_of_table = 0
    for guest in table:
        for item in table[guest]:
            price_of_item = get_item_price(item)
            price_of_table += price_of_item
            item_line = '{:<30} {} {:>5}'.format(item, "$", price_of_item)
            print(item_line)

    tax = price_of_table * .07
    total = price_of_table + tax

    good_tip = ("%.2f" % (total * .25))
    ok_tip = ("%.2f" % (total * .2))
    bad_tip = ("%.2f" % (total * .15))

    print("")

    price_formatted = ("%.2f" % price_of_table)
    tax_formatted = ("%.2f" % tax)
    total_formatted = ("%.2f" % total)

    print('{:<15} {} {} {:>5}'.format(" ", "Price: ", "$", price_formatted))
    print('{:<15} {} {} {:>5}'.format(" ", "Taxes: ", "$", tax_formatted))
    print('{:<15} {} {} {:>5}'.format(" ", "Total: ", "$", total_formatted))
    print("**Suggested Tip**")
    print('{:<10} {:>5}'.format("Tip 25%:", good_tip))
    print('{:<10} {:>5}'.format("Tip 20%:", ok_tip))
    print('{:<10} {:>5}'.format("Tip 15%:", bad_tip))


table1 = {
    "Guest 1": ["Eggs Benedict", "Coffee"],
    "Guest 2": ["Biscuit and Gravy", "Coffee"],
    "Guest 3": ["Steak and Eggs", "Coffee"]
}


table2 = {
    "Guest 1": ["Steak Salad", "Soft Drink"],
    "Guest 2": ["Soup of the Day", "Chicken Wrap", "Water"],
    "Guest 3": ["Chicken Fingers", "Soft Drink"],
    "For the Table": ["Chef Special"]
}


get_receipt(table2)
