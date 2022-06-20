import utils
from persons import Worker


def print_workers_menu():
    print("""Options:
    1 - Log In
    2 - Add new worker
    3 - Return to main menu""")


def workers_menu(workers, box_list):
    response = 0
    while response != 3:
        print_workers_menu()
        response = utils.int_input()
        if response == 1:
            name = input("Whats your name?")
            n_response = 0
            while n_response != 4:
                n_response = int(input("""Options:
                1 - Sign In 
                2 - Sign Out
                3 - View Info
                4 - Exit\n"""))
                if n_response == 1:
                    workers[name].sign_in()
                    for box in box_list.box_list:
                        if box.current_worker is None:
                            box.current_worker = name
                elif n_response == 2:
                    workers[name].sign_out()
                elif n_response == 3:
                    workers[name].print_info()
        elif response == 2:
            new_worker = Worker()
            workers[new_worker.name] = new_worker
            print(f"Welcome {new_worker.name}!")
