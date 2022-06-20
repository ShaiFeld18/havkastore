import utils
from persons import Customer



class Line:
    def __init__(self):
        self.line = []

    def add_to_queue(self):
        new_customer = Customer()
        if new_customer.can_enter():
            self.line.append(new_customer)
        else:
            print("Sorry, you can't enter the store!")

    def admit_customers(self, num_customers, boxes_list):
        if len(self.line) > num_customers:
            print("Not enough customers :(")
        else:
            for i in range(num_customers):
                print(f"{self.line[0].name}, please enter")
                boxes_list.add_customer(self.line[0].name)
                self.line.pop(0)

    def print_waiting_list(self):
        for customer in self.line:
            print(customer.name)


def print_queue_menu():
    print("""Options:
    1 - Add customer to line
    2 - Let in customers
    3 - Print waiting line
    4 - Return to main menu""")


def queue_menu(line, boxes_list):
    response = 0
    while response != 4:
        print_queue_menu()
        response = utils.int_input()
        if response == 1:
            line.add_to_queue()
        elif response == 2:
            print("How many customers? ")
            n = utils.int_input()
            line.admit_customers(n, boxes_list)
        elif response == 3:
            line.print_waiting_list()
        elif response != 4:
            print("Wrong input")
    print('Thank you for using my app!')
