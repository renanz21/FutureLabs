from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///accounting.db"
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, default=0, nullable=False)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, nullable=False, default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    value = db.Column(db.Float, unique=False, nullable=False)

def get_account():
    return Account.query.first()

def total_stock():
    return sum(p.quantity for p in Product.query.all())

@app.route("/")
def index():
    account = get_account()
    return render_template(
        "index.html",
        stock_level=total_stock(),
        balance=round(account.balance, 2),
    )

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    if request.method == "POST":
        try:
            name = request.form["product"].strip()
            price = float(request.form["price"])
            qty = int(request.form["quantity"])

            if not name or price <= 0 or qty <= 0:
                raise ValueError

            account = get_account()
            total_cost = price * qty
            account.balance -= total_cost

            product = Product.query.filter_by(name=name).first()
            if not product:
                product = Product(name=name, quantity=0)
                db.session.add(product)

            product.quantity += qty

            db.session.add(Transaction(
                type="Purchase",
                description=f"Purchased {qty} {name} for €{price}",
                value=-total_cost,
            ))

            db.session.commit()
            return redirect(url_for("index"))

        except (ValueError, SQLAlchemyError):
            db.session.rollback()
            return render_template("purchase.html", error="Invalid purchase data.")

    return render_template("purchase.html")

@app.route("/sales", methods=["GET", "POST"])
def sale():
    if request.method == "POST":
        try:
            name = request.form["product"].strip()
            price = float(request.form["price"])
            qty = int(request.form["quantity"])

            product = Product.query.filter_by(name=name).first()
            if not product or qty <= 0 or price <= 0 or product.quantity < qty:
                raise ValueError

            account = get_account()
            total_income = price * qty
            account.balance += total_income
            product.quantity -= qty

            db.session.add(Transaction(
                type="Sale",
                description=f"Sold {qty} {name} for €{price}",
                value=total_income,
            ))

            db.session.commit()
            return redirect(url_for("index"))

        except (ValueError, SQLAlchemyError):
            db.session.rollback()
            return render_template("sales.html", error="Invalid sale data.")

    return render_template("sales.html")

@app.route("/balance", methods=["GET", "POST"])
def change_balance():
    if request.method == "POST":
        try:
            op = request.form["operation"]
            amount = float(request.form["amount"])

            if amount <= 0 or op not in ("add", "subtract"):
                raise ValueError

            account = get_account()
            value = amount if op == "add" else -amount
            account.balance += value

            db.session.add(Transaction(
                type="Balance",
                description=f"{op.capitalize()} balance",
                value=value,
            ))

            db.session.commit()
            return redirect(url_for("index"))

        except (ValueError, SQLAlchemyError):
            db.session.rollback()
            return render_template("balance.html", error="Invalid balance operation.")

    return render_template("balance.html")

@app.route("/history/")
@app.route("/history/<int:line_from>/<int:line_to>/")
def history(line_from=None, line_to=None):
    query = Transaction.query.order_by(Transaction.id)

    if line_from is not None and line_to is not None:
        query = query.slice(line_from - 1, line_to)

    transactions = query.all()

    return render_template(
        "history.html",
        history=transactions
    )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        if Account.query.first() is None:
            db.session.add(Account(balance=0.0))
            db.session.commit()

    app.run()