def int_input():
    x = input()
    try:
        return int(x)
    except ValueError:
        print("Wrong input :(")
