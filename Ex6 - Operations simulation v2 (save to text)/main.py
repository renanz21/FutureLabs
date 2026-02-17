from st import load_data, save_data
from op import deposit, withdraw, add_item, remove_item, print_menu

balance_file = "balance.txt"
inventory_file = "inventory.txt"
history_file = "history.txt"

def main():

    balance = load_data(balance_file, 0)
    inventory = load_data(inventory_file, {})
    history = load_data(history_file, [])

    print("Commands: deposit, withdraw, add, remove, show, end")

    while True:
        command = input("Command: ").strip().lower()

        if command == "deposit":
            amount = float(input("Amount: "))
            balance = deposit(balance, amount, history)
            print_menu()

        elif command == "withdraw":
            amount = float(input("Amount: "))
            balance = withdraw(balance, amount, history)
            print_menu()

        elif command == "add":
            item = input("Item name: ")
            qty = int(input("Quantity: "))
            add_item(inventory, item, qty, history)
            print_menu()

        elif command == "remove":
            item = input("Item name: ")
            qty = int(input("Quantity: "))
            remove_item(inventory, item, qty, history)
            print_menu()

        elif command == "show":
            print("Balance: ", balance)
            print("Inventory: ")
            for item, qty in inventory.items():
                print(f"- {qty}x: {item}")
            print("History: ")
            for entry in history:
                print("-", entry)
            print_menu()

        elif command == "end":
            shutdown(balance, inventory, history)
            print("Program halted")
            return

        else:
            print("Invalid command, try again or type 'end' to exit")
            print_menu()

def shutdown(balance, inventory, history):

    save_data(balance_file, balance)
    save_data(inventory_file, inventory)
    save_data(history_file, history)

if __name__ == "__main__":
    main()