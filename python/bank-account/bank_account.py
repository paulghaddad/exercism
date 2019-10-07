import functools
from threading import Lock


class BankAccount(object):

    def check_if_closed(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args[0].closed or args[0].closed is None:
                raise ValueError("The account is closed.")
            return func(*args, **kwargs)
        return wrapper


    def check_if_open(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args[0].closed is False:
                raise ValueError("The account is not closed.")
            return func(*args, **kwargs)
        return wrapper


    def __init__(self):
        self.closed = None
        self.lock = Lock()


    @check_if_open
    def open(self):
        self.closed = False
        self.balance = 0


    @check_if_closed
    def get_balance(self):
        return self.balance


    @check_if_closed
    def deposit(self, amount):
        with self.lock:
            if amount < 0:
                raise ValueError("This is an invalid deposit amount.")

            self.balance += amount


    @check_if_closed
    def withdraw(self, amount):
        with self.lock:
            if amount > self.balance or amount < 0:
                raise ValueError("This amount cannot be withdrawn.")

            self.balance -= amount


    @check_if_closed
    def close(self):
        self.closed = True
