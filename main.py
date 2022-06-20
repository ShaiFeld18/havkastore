import queue_app
import workers_app
import box_app
import utils
from queue_app import Line
from box_app import AllBoxes


def print_main_menu():
    print("""Options:
    1 - Open queue menu
    2 - Open box menu
    3 - Open workers menu
    4 - Exit""")


line = Line()
workers = {}
boxes = AllBoxes()
response = 0
while response != 4:
    try:
        print_main_menu()
        response = utils.int_input()
        if response == 1:
            queue_app.queue_menu(line, boxes)
        elif response == 2:
            box_app.box_menu(boxes)
        elif response == 3:
            workers_app.workers_menu(workers, boxes)
    except:
        print("An error occurred, try again")
