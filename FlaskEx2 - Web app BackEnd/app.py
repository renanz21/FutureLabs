from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

history_file = "history.txt"

balance = 0
stock = {}

def read_history():
    if not os.path.exists(history_file):
        return []
    try:
        with open(history_file, "r") as fd:
            return fd.readlines()
    except IOError:
        return []

def write_history(entry):
    try:
        with open(history_file, "a") as fd:
            fd.write(entry + "\n")
    except IOError:
        pass

def total_stock():
    return sum(stock.values())

@app.route("/")
def index():
    return render_template(
        "index.html",
        stock_level=total_stock(),
        balance=round(balance, 2)
    )

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    global balance, stock

    if request.method == "POST":
        try:
            product = request.form["product"].strip()
            price = float(request.form["price"])
            quantity = int(request.form["quantity"])

            if not product or price <= 0 or quantity <= 0:
                raise ValueError

            total_cost = price * quantity
            balance -= total_cost
            stock[product] = stock.get(product, 0) + quantity

            write_history(
                f"Purchase | {product} | Quantity={quantity} | Price={price:.2f} | Total={-total_cost:.2f}"
            )
            return redirect(url_for("index"))

        except (ValueError, KeyError):
            return render_template("purchase.html", error="Invalid purchase data.")

    return render_template("purchase.html")

@app.route("/sales", methods=["GET", "POST"])
def sale():
    global balance, stock

    if request.method == "POST":
        try:
            product = request.form["product"].strip()
            price = float(request.form["price"])
            quantity = int(request.form["quantity"])

            if (
                not product
                or price <= 0
                or quantity <= 0
                or stock.get(product, 0) < quantity
            ):
                raise ValueError

            total_income = price * quantity
            balance += total_income
            stock[product] -= quantity

            write_history(
                f"Sale | {product} | Quantity={quantity} | Price={price:.2f} | Total={total_income:.2f}"
            )
            return redirect(url_for("index"))

        except (ValueError, KeyError):
            return render_template("sales.html", error="Invalid sale data.")

    return render_template("sales.html")

@app.route("/balance", methods=["GET", "POST"])
def change_balance():
    global balance

    if request.method == "POST":
        try:
            operation = request.form["operation"]
            amount = float(request.form["amount"])

            if amount <= 0 or operation not in ("add", "subtract"):
                raise ValueError

            if operation == "add":
                balance += amount
            else:
                balance -= amount

            write_history(
                f"Balance | {operation} | Amount={amount:.2f}"
            )
            return redirect(url_for("index"))

        except (ValueError, KeyError):
            return render_template("balance.html", error="Invalid balance operation.")

    return render_template("balance.html")

@app.route("/history/")
@app.route("/history/<int:line_from>/<int:line_to>/")
def history(line_from=None, line_to=None):
    lines = read_history()

    if line_from is not None and line_to is not None:
        start = max(line_from - 1, 0)
        end = min(line_to, len(lines))
        lines = lines[start:end]

    history_entries = []
    for line in lines:
        history_entries.append({
            "type": line.split("|")[0].strip(),
            "description": line.strip(),
            "value": ""
        })

    return render_template("history.html", history=history_entries)

if __name__ == "__main__":
    app.run()