class Color:
    Reset = "\033[0m"
    Red = "\033[031m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Magenta = "\033[35m"
    Cyan = "\033[96m"

def linear_search(l, target): # l means list
    print(f"list: {Color.Green}{l}{Color.Reset}")
    print(f"target: {Color.Red}{target}{Color.Reset}")
    for i in range(len(l)):
        print(f"is {Color.Cyan}{l[i]}{Color.Reset} == target ({Color.Red}{target}{Color.Reset})?")
        if l[i] == target:
            print("yes")
            return i # index of target
        print("no")
    return -1

nums = [5, 22, 10, 1, 0, 50, 100, 44, 70]
#       0   1  2   3  4   5    6   7   8

print(linear_search(nums, 70))
