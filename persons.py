import datetime


class Person:
    def __init__(self):
        self.name = input("Whats your name? ")
        t = float(input("Whats your temperature? "))
        if t > 47.5:
            print('You cant enter')
            return
        else:
            self.temperature = t
        m = input("Do you have a mask? y/n ")
        if m == 'n':
            print('You cant enter')
            return
        else:
            self.mask = True
        q = input("Do you need quarantine? y/n ")
        if q == 'y':
            print('You cant enter')
            return
        else:
            self.quarantine = True


class Customer(Person):
    pass


class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        self.ins = []
        self.outs = []
        self.debt = 0

    def sign_in(self):
        temp = int(input("Whats your temperature? "))
        m = input("Do you have a mask? y/n ")
        q = input("Do you need quarantine? y/n ")
        if temp <= 38 and m == 'y' and q == 'n':
            self.ins.append(datetime.datetime.now())
            print('Signed In')
        else:
            self.debt += 40
            print("You can't enter, you've been fined 40 shekel")

    def sign_out(self):
        self.outs.append(datetime.datetime.now())
        print("Signed out")

    def print_history(self):
        print(f'In\t\t\tOut')
        for i in range(len(self.ins)):
            if len(self.outs) < i:
                out = None
            else:
                out = self.outs[i]
            print(f'{self.ins[i]}\t\t\t{out}')

    def print_info(self):
        print(f"""
               Name:{self.name},
               Debt: {self.debt}$,
               Work History:""")
        self.print_history()
