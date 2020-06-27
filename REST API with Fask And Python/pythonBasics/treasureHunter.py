inventory = {
    "rope": 1,
    "coin": 10,
    "ruby": 2
}

def add_item(item = "coin", amount_found = 1):
    item = item.lower()

    if item in inventory:
        current_quantity = inventory[item]
        inventory[item] = current_quantity + amount_found
    else:
        inventory[item] = amount_found

def print_item(item):
    item = item.lower()

    if item not in inventory:
        print(f"The adventurer doesn't have a {item}")
    else:
        quantity = inventory[item]
        print(f"{item.capitalize()}: {quantity}")

def print_all_items():
    print("-- Items in inventory --")
    for item in inventory:
        item.lower()
        quantity = inventory[item]
        print(f"{item.capitalize()}: {quantity}")

print_all_items()
add_item("dagger")
print_item("coin")
print_all_items()