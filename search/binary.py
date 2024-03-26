def binary_search(l, target):  # l means list

    left_pointer = 0
    right_pointer = len(l) - 1  #  index of last element

    while left_pointer <= right_pointer:
        midpoint = left_pointer + (right_pointer - left_pointer) // 2
        if l[midpoint] == target:
            return midpoint
        # change the searchable section of the list
        elif l[midpoint] > target:
            right_pointer = midpoint - 1  # right_pointer of searchable part of list is brought to the midpoint and one shorter because the code already confirmed that the target isn't at the midpoint
        else:
            left_pointer = midpoint + 1  #  otherwise the left_pointer of the searchable part of the list is brought to midpoint and one further along because target cannot be at the midpoint in this case

    return -1


nums = [1, 2, 3, 38, 48, 51, 53, 61, 62, 65, 72, 73, 83, 83, 93]
#       0  1  2  3   4   5   6   7   8   9   10  11  12  13  14

for i in range(len(nums)):
    print(binary_search(nums, nums[i]))


letters = ["a", "b", "c", "d", "e"]
print(binary_search(letters, "b"))
