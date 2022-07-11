def int_input():
    x = input('Your choice: ')
    try:
        return int(x)
    except ValueError:
        print("Wrong input :(")


def run_menu(menu, printable):
    for key in printable.keys:
        print(key, '--', printable[key])
    res = int_input()
    if res == len(menu)+1:
        return None
    try:
        do = menu.get(res)
        do()
    except:
        print('An error has occurred, returning to main menu')
        return 'run'
