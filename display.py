import os


# colors
RESET = "\033[0m"
BLACK = "\033[0;30;0m"
GREEN = "\033[0;32m"
RED = "\033[0;31;47m"

cols, rows = os.get_terminal_size()


def print_das():
    for _ in range(cols):
        print(f"{BLACK}─{RESET}", end='')
    print("")


def print_run():
    xx = "Running Program"
    xx = xx.center(int(cols))
    print(xx)
    print_das()


def sucess_msg():
    xx = f"Compilation {GREEN}Successful ✔{RESET}"
    xx = xx.center(int(cols))
    print_das()
    print(xx)
    print_das()


def failed_msg():
    xx = f"Compilation {RED}Failed ❌{RESET}"
    xx = xx.center(int(cols))
    print_das()
    print(xx)
    print_das()
