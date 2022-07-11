from queue_app import Line
from box_app import AllBoxes
import workers_app
import box_app
from utils import run_menu


line = Line()
boxes = AllBoxes()

queue_menu = {1: line.add_to_queue(),
              2: line.admit_customers(),
              3: line.print_waiting_list()}
queue_printable = {1: 'Add customer to queue',
                   2: 'Admit customer to box',
                   3: 'Print Waiting List',
                   4: 'Return to main menu'}

boxes_menu = {1: boxes.add_box(),
              2: boxes.status(),
              3: boxes.history(),
              4: boxes.corona()}
boxes_printable = {1: 'Create new box',
                   2: 'Show boxes status',
                   3: 'Print history',
                   4: 'Check for corona',
                   5: 'Return to main menu'}

workers_menu = {1: workers.login(),
                2: workers.new_worker()}
workers_printable = {1: 'Log In',
                     2: 'Add new customer',
                     3: 'Return to main menu'}

printable_main = {1: 'Open queue menu',
                  2: 'Open boxes menu',
                  3: 'Open customers menu',
                  4: 'Exit app'}
main_menu = {1: run_menu(queue_menu, queue_printable),
             2: run_menu(boxes_menu, boxes_printable),
             3: run_menu(workers_menu, workers_printable)}

x = 'run'
while x == 'run':
    x = run_menu(main_menu)
