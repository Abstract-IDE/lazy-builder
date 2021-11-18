import os
from colorama import Fore as colors


cols, rows = os.get_terminal_size()


def print_das():
    for _ in range(cols):
        print(colors.BLACK+"─"+colors.RESET, end="")
    print("")


def print_run():
    xx = "Running Program"
    xx = xx.center(int(cols))
    print(xx)
    print_das()


def sucess_msg():
    xx = "Compilation " + colors.GREEN + "Successful ✔" + colors.RESET
    xx = xx.center(int(cols))
    print_das()
    print(xx)
    print_das()


def failed_msg():
    xx = "Compilation " + colors.RED + "Failed ❌" + colors.RESET
    xx = xx.center(int(cols))
    print_das()
    print(xx)
    print_das()
