import datetime

import pandas as pd

import utils


class Box:
    def __init__(self, num):
        self.num = num
        self.current_worker = None
        self.current_customer = None


class AllBoxes:
    def __init__(self):
        self.box_list = []
        self.history = pd.DataFrame(columns=['box', 'worker', 'customer', 'date'])

    def add_box(self):
        self.box_list.append(Box(len(self.box_list)+1))
        print('Box added successfully!')

    def add_customer(self, new_customer):
        for box in self.box_list:
            if box.current_customer is None:
                box.current_customer = new_customer
                self.history = self.history.append({'box': box.num,
                                                    'worker': box.current_worker,
                                                    'customer': box.current_customer,
                                                    'date': datetime.datetime.now()}, ignore_index=True)
                return None
        print("No empty box")


def box_menu(boxes):
    response = 0
    while response != 5:
        print("""Option:
        1 - Add box
        2 - Display box status
        3 - Display history
        4 - Check corona history
        5 - Return to main menu""")
        response = utils.int_input()
        if response == 1:
            boxes.add_box()
        elif response == 2:
            print("Enter box num:")
            num = utils.int_input()
            b = boxes.box_list[num-1]
            print(f"""Num: {b.num},
            Current Worker: {b.current_worker},
            Current Customer: {b.current_customer}""")
        elif response == 3:
            print(boxes.history)
        elif response == 4:
            sick = input('Which worker is sick?')
            print(boxes.history[boxes.history['worker'] == sick])
