import pandas as pd
import datetime


class Person:
    def __init__(self):
        self.name = input("Whats your name? ")
        self.temp = int(input("Whats your temperature? "))
        m = input("Do you have a mask? y/n ")
        if m == 'y':
            self.mask = True
        else:
            self.mask = False
        q = input("Do you need quarantine? y/n ")
        if q == 'y':
            self.quarantine = True
        else:
            self.quarantine = False

    def can_enter(self):
        if self.temp <= 38 and self.mask and self.quarantine is False:
            return True
        return False


class Customer(Person):
    pass


class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        self.signs = pd.DataFrame(columns=['In', 'Out'])
        self.debt = 0

    def sign_in(self):
        temp = int(input("Whats your temperature? "))
        m = input("Do you have a mask? y/n ")
        q = input("Do you need quarantine? y/n ")
        if temp <= 38 and m == 'y' and q == 'n':
            self.signs.loc[len(self.signs.index)] = [datetime.datetime.now(), None]
            print('Signed In!')
        else:
            self.debt += 40
            print("You can't enter, you've been fined 40 shekel")

    def sign_out(self):
        self.signs.iloc[len(self.signs.index)-1, 1] = datetime.datetime.now()
        print("Signed out!")

    def print_info(self):
        print(f"""Name:{self.name},
Debt: {self.debt},
Work History:\n {self.signs.to_string()}""")
