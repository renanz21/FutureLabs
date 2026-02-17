from op import *

class Manager:
    def __init__(self, balance=0, inventory=None, history=None):
        self.balance = balance
        self.inventory = inventory if inventory is not None else {}
        self.history = history if history is not None else []
        self._actions = {}
        self._register_actions()

    def action(self, name):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                self.history.append(f"Action: {name}")
                return result

            self._actions[name] = wrapper
            return wrapper
        return decorator

    def assign(self, task_name, *args, **kwargs):
        if task_name not in self._actions:
            raise ValueError("Task not found")

        return self._actions[task_name](*args, **kwargs)

    def _register_actions(self):

        @self.action("deposit")
        def _deposit(amount):
            self.balance = deposit(self.balance, amount, self.history)
            print("Deposit succeeded")
            return self.balance

        @self.action("withdraw")
        def _withdraw(amount):
            self.balance = withdraw(self.balance, amount, self.history)
            print("Withdraw succeeded")
            return self.balance

        @self.action("purchase")
        def _purchase(item, qty, price_per_unit):
            total_cost = qty * price_per_unit

            if total_cost > self.balance:
                self.history.append("Purchase failed: no balance")
                return self.balance

            self.balance -= total_cost
            add_item(self.inventory, item, qty, self.history)
            print("Purchase succeeded")
            return self.balance

        @self.action("sale")
        def _sale(item, qty, price_per_unit):
            if item not in self.inventory or self.inventory[item] < qty:
                self.history.append("Sale failed, no inventory")
                return self.balance

            remove_item(self.inventory, item, qty, self.history)
            revenue = qty * price_per_unit
            self.balance += revenue
            print("Sale succeeded")
            return self.balance

        @self.action("balance")
        def _balance():
            return self.balance