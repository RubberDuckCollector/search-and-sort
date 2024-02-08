class Color:
    Red = "\033[031m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[96m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"
    Warn = "\033[93m"
    Underline = "\033[4m"
    Bold = "\033[1m"
    Hidden = "\033[8m"
    Blink = "\033[5m"
    Dim = "\033[2m"
    Reverse = "\033[7m"
    Reset = "\033[0m"


# returns a tuple of the sorted list and the number of passes it took
def bubble_sort_walkthrough(input_list: list) -> tuple:
    pass_num = 0
    for i in range(len(input_list) - 1):
        pass_num += 1
        print(f"{Color.Yellow}PASS {pass_num}{Color.Reset}")
        for j in range(len(input_list) - i - 1):
            print(f"the list: {Color.Cyan}{input_list}{Color.Reset}")
            print("")
            input(f"{Color.LightRed}Current{Color.Reset} value we're looking at: {Color.Yellow}{
                  input_list[j]}{Color.Reset} ({Color.Dim}index{Color.Reset} {Color.Underline}{Color.LightBlue}{j}{Color.Reset}) {Color.Dim}(press ENTER to continue){Color.Reset}")
            print("")
            input(f"Value at the {Color.LightRed}next index{Color.Reset} of the list: {Color.Yellow}{
                input_list[j + 1]}{Color.Reset} ({Color.Dim}index{Color.Reset} {Color.LightBlue}{Color.Underline}{j + 1}{Color.Reset}) {Color.Dim}(press ENTER to continue){Color.Reset}")
            print("")
            if input_list[j] > input_list[j + 1]:  # if a swap needs to be made
                input(
                    f"{Color.Underline}{Color.LightMagenta}The current value is bigger than the one after it! Swap them!{Color.Reset} {Color.Dim}(press ENTER to continue){Color.Reset}")
                print("")
                # normal way to swap variables
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
            else:
                input(f"{Color.LightGreen}{Color.Underline}{input_list[j]} < {input_list[j + 1]}: No swaps need to be made.{Color.Reset} {
                    Color.Dim}(press ENTER to continue){Color.Reset}")
                print("")

    sorted_list = input_list

    return sorted_list, pass_num


def main():
    print("Sorting in ascending order.\n")

    nums = [9, 5, 3, 7, 2, 8, 4, 1, 6, 0]
    print("Sorted list:")
    sorted_nums = bubble_sort_walkthrough(nums)
    print(f"Algorithm exited after {
          sorted_nums[1]} passes. Sorted list:\n{sorted_nums[0]}")


if __name__ == '__main__':
    main()
