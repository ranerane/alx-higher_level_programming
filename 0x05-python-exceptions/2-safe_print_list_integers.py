#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Function that prints the first x elements of a list and only integers.
    """
    try:
        count = 0
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return (count)
    except TypeError:
        print("You have a type error!")
