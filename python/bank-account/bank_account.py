import functools
from threading import Lock


class BankAccount(object):
    lock = Lock()

    def check_if_closed(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args[0].closed:
                raise ValueError("The account is closed.")
            return func(*args, **kwargs)
        return wrapper


    def check_if_open(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not args[0].closed:
                raise ValueError("The account is not closed.")
            return func(*args, **kwargs)
        return wrapper


    def __init__(self):
        self.closed = True

    @check_if_closed
    def get_balance(self):
        return self.balance


    @check_if_open
    def open(self):
        self.closed = False
        self.balance = 0


    @check_if_closed
    def deposit(self, amount):
        with BankAccount.lock:
            if amount < 0:
                raise ValueError("This is an invalid deposit amount.")

            self.balance += amount


    @check_if_closed
    def withdraw(self, amount):
        with BankAccount.lock:
            if amount > self.balance or amount < 0:
                raise ValueError("This amount cannot be withdrawn.")

            self.balance -= amount


    @check_if_closed
    def close(self):
        self.closed = True
