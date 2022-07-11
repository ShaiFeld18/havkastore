import datetime


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



