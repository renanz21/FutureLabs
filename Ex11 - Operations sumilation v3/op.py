def deposit(balance, amount, history):
    balance += amount
    history.append(f"Deposited {amount}")
    return balance

def withdraw(balance, amount, history):
    if amount > balance:
        history.append(f"Withdrawn failed: insufficient balance")
        print("Withdrawn failed: insufficient balance")
        return balance

    balance -= amount
    history.append(f"Withdrew {amount}")
    return balance

def add_item(inventory, item, qty, history):
    inventory[item] = inventory.get(item, 0) + qty
    history.append(f"Added {qty} of {item}")

def remove_item(inventory, item, qty, history):
    if item not in inventory or inventory[item] < qty:
        history.append(f"Removed failed for {item}")
        print(f"Removed failed for {item}, quantity in stock is lower than {qty}")
        return

    inventory[item] -= qty

    if inventory[item] == 0:
        del inventory[item]

    history.append(f"Removed {qty} of {item}")

def print_menu():
    print("Commands: deposit, withdraw, add, remove, show, manager, end")

def print_menu_man():
    print("Commands [Management]: deposit, withdraw, purchase, sale, balance, back")