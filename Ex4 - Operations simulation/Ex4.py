bal = 0
war = {}
prod = set()
op = []

print("Options: ")
print("balance")
print("sale")
print("purchase")
print("account")
print("list")
print("warehouse")
print("review")
print("end")

# noinspection PyUnreachableCode
while True:

    cmd = input("Enter option: ").strip().lower() # Input will have spaced removed and letters in lower case to match the options

    # Code for balance

    if cmd == "balance":
        try:
            amount = float(input("Enter amount: "))
            bal += amount
            op.append(("balance", amount))
        except ValueError:
            print("Invalid input. Options must be a number")

        # Reprint options
        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue

    #Code for sale

    elif cmd == "sale":
        name = input("Product name: ").strip()
        if not name: #Empty input returns false
            print("Invalid input, input cannot be empty")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        try:
            price = float(input("Product price: "))
            qty = float(input("Quantity sold: "))
        except ValueError:
            print("Invalid price or quantity")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        if qty <= 0:
            print("Invalid quantity, quantity must be more than 0")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        if name not in war or war[name]["quantity"] < qty:
            print("Not enough stock")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        war[name]["quantity"] -= qty
        rev = price * qty
        bal += rev
        op.append(("sale", name, price, qty))

        print(f"Sale completed, revenue is {rev}")
        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue

    #Code for purchase

    elif cmd == "purchase":
        name = input("Product name: ").strip()
        if not name:
            print("Invalid input, input cannot be empty")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        try:
            price = float(input("Product price: "))
            qty = float(input("Quantity sold: "))
        except ValueError:
            print("Invalid price or quantity")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        if qty <= 0:
            print("Invalid quantity, quantity must be more than 0")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        cost = price * qty

        if bal - cost < 0:
            print("Insufficient funds, transaction denied")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        bal -= cost
        prod.add(name)

        if name not in war:
            war[name] = {"price": price, "quantity": qty}
        else:
            war[name]["price"] = price
            war[name]["quantity"] += qty

        op.append(("purchase", name, price, qty))
        print(f"Purchase completed, cost: {cost}")

        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue

    #Code for balance

    elif cmd == "account":
        print(f"Account balance: {bal}")

        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue

    #Code for list

    elif cmd == "list":
        if not war:
            print("Warehouse is empty")
        else:
            print("Warehouse Inventory")
            for product, data in war.items():
                print(f"{product} - Price: {data['price']}, Quantity: {data['quantity']}")

        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue

    # Code for warehouse
    elif cmd == "warehouse":
        name = input("Enter product to show: ").strip()

        if name in war:
            print(f"{name}: Price = {war[name]['price']}, Quantity = {war[name]['quantity']}")
        else:
            print("Product not found")

        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue

    # Code for review
    elif cmd == "review":

        start = input("Enter index to begin search (leave empty to start on first index): ").strip()
        end = input("Enter index to end search (leave empty to end on last index): ").strip()

        try:
            start_i = int(start) if start else 0
            end_i = int(end) if end else len(op)
        except ValueError:
            print("Invalid index")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        if start_i < 0 or end_i > len(op) or start_i > end_i:
            print("Index out of range")
            print("\nOptions: ")
            print("\nbalance")
            print("sale")
            print("purchase")
            print("account")
            print("list")
            print("warehouse")
            print("review")
            print("end")
            continue

        print("Operations history:")
        for idx, oper in enumerate(op[start_i:end_i], start_i):
            if oper[0] == "balance":
                oper_id, oper_c = oper
                print(f"Transaction ID:{idx} - Operation: {oper_id}, Balance added:{oper_c}")
            elif oper[0] == "purchase":
                oper_id, oper_item, oper_price, oper_qty = oper
                print(f"Transaction ID:{idx} - Operation: {oper_id}, Item acquired:{oper_item}, Price:{oper_price}, Quantity:{oper_qty}")
            else:
                oper_id, oper_item, oper_price, oper_qty = oper
                print(f"Transaction ID:{idx} - Operation: {oper_id}, Item sold:{oper_item}, Price:{oper_price}, Quantity:{oper_qty}")

        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue

    #Line to stop program

    elif cmd == "end":
        print("Program halted")
        break

    else:
        print("Invalid Input. Choose one of the options below")
        print("\nOptions: ")
        print("\nbalance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse")
        print("review")
        print("end")
        continue


