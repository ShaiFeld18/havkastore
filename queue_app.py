from persons import Customer


class Line:
    def __init__(self):
        self.line = []

    def add_to_queue(self):
        new_customer = Customer()
        self.line.append(new_customer)

    def admit_customers(self, num_customers, boxes_list):
        if len(self.line) > num_customers:
            print("Not enough customers")
        else:
            for i in range(num_customers):
                print(f"{self.line[0].name}, please enter")
                boxes_list.add_customer(self.line[0].name)
                self.line.pop(0)

    def print_waiting_list(self):
        for customer in self.line:
            print(customer.name)
