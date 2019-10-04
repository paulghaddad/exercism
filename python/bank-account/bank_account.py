from threading import Lock


class BankAccount(object):
    lock = Lock()

    def __init__(self):
        self.closed = True

    def get_balance(self):
        if self.closed:
            raise ValueError("The account is closed.")

        return self.balance

    def open(self):
        if not self.closed:
            raise ValueError("The account is closed.")

        self.closed = False
        self.balance = 0

    def deposit(self, amount):
        with BankAccount.lock:
            if self.closed:
                raise ValueError("The account is closed.")

            if amount < 0:
                raise ValueError("This is an invalid deposit amount.")

            self.balance += amount

    def withdraw(self, amount):
        with BankAccount.lock:
            if self.closed:
                raise ValueError("The account is closed.")

            if amount > self.balance or amount < 0:
                raise ValueError("This amount cannot be withdrawn.")

            self.balance -= amount

    def close(self):
        if self.closed:
            raise ValueError("The account is closed.")

        self.closed = True
