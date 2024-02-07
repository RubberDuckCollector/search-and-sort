import timeit
import numpy as np
from random import randint
import matplotlib.pyplot as plt


def linear_search(
    nums: list, target: int
) -> int:  # takes in list return type is int (index of target)
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def main():
    with open("test-list.txt", "r") as f:
        my_list = f.read()

    my_list = list(my_list)

    with open("timeit-data-linear-search.txt", "w") as f:
        for i in range(len(my_list)):
            starttime = timeit.default_timer()
            linear_search(my_list, i)
            print(
                f"time taken to find {i} in my_list:",
                timeit.default_timer() - starttime,
            )


if __name__ == "__main__":
    main()
