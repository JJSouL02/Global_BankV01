class Cuenta:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance
        self.transactions = []

    def get_balance(self, password):
        if password == self.password:
            return f"Your balance is: {self.balance}"
        else:
            return "Incorrect password"

    def deposit(self, amount, password):
        if amount < 0:
            return "You cannot deposit a negative amount!"
        if password != self.password:
            return "Incorrect password"
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return f"Your new balance is: {self.balance}"

    def withdraw(self, amount, password):
        if amount < 0:
            return "You cannot withdraw a negative amount"
        if password != self.password:
            return "Incorrect password for this account"
        if amount > self.balance:
            return "You cannot withdraw more than you have in your account"
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        return f"Your new balance is: {self.balance}"

    def show_account(self):
        return f"Name: {self.name}\nBalance: {self.balance}"

    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
            return "Password changed successfully."
        else:
            return "Incorrect old password."

    def get_transactions(self, password):
        if password == self.password:
            return "\n".join(self.transactions)
        else:
            return "Incorrect password"