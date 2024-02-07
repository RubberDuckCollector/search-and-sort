class Color:
    Reset = "\033[0m"
    Red = "\033[031m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Magenta = "\033[35m"
    Cyan = "\033[96m"

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while j >= i and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)
    return arr

nums = [9, 5, 4, 15, 3, 8, 11]

print(quick_sort(nums, 0, len(nums)-1))
