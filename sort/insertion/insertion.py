import time
from random import randint

"""
this is an abstracted demonstration of insertion sort. in the output the user does not
see precisely what happens when the element "moves down the list".
the user thinks the sorted item
barges into its correct index, shoving all elements on its right up by 1 index.
"""

# colours make the output easier to read


class Color:
    Reset = "\033[0m"
    Red = "\033[031m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Magenta = "\033[35m"
    Cyan = "\033[96m"

# takes list parameter l and returns a list


def insertion_sort(l: list):

    # the insertion sort for loop runs len(list)-1 times
    for i in range(1, len(l)):
        print(f"list: {Color.Red}{l}{Color.Reset}\n")
        time.sleep(1)

        # consider this value of the list
        current_vaule = l[i]
        print(f"current_value: {Color.Yellow}{current_vaule}{
              Color.Reset} (looking at this value to sort on this pass)")
        time.sleep(1)
        # sorting smallest to largest so if its already sorted
        if l[i-1] < current_vaule:
            print(f"{Color.Yellow}{current_vaule}{Color.Reset} does {Color.Green}NOT{
                  Color.Reset} need to be sorted (it's {Color.Green}bigger{Color.Reset} than the value on its left)\n")
            time.sleep(1)
            print("no changes to the list.")
            time.sleep(1)
        # if it's not sorted
        else:
            print(f"{Color.Yellow}{current_vaule}{Color.Reset} {Color.Magenta}DOES{
                  Color.Reset} need to be sorted (it's {Color.Magenta}smaller{Color.Reset} than the value on its left)")
            time.sleep(1)
            while l[i-1] > current_vaule and i > 0:

                print(f"index of {current_vaule}: {i}")
                print(f"i before minus: {i}")
                time.sleep(1)
                l[i] = l[i-1]
                i -= 1
                print(f"i after minus: {i}")
                time.sleep(1)
                print(f"put {current_vaule} at index {i}.")
            l[i] = current_vaule
            time.sleep(1)

    return f"sorted list: {Color.Cyan}{l}{Color.Reset}\n"


def main():

    nums = [3, 10, 4, 2, 5, 8]
    print(insertion_sort(nums))

    # nums2 = [randint(0, 100) for i in range(15)]
    # print(insertion_sort(nums2))


if __name__ == '__main__':
    main()
