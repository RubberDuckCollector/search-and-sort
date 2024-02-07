import random


# Function to shuffle the list
def shuffle_list(lst):
    shuffled_list = lst[:]  # Create a copy of the original list
    random.shuffle(shuffled_list)  # Shuffle the copied list
    return shuffled_list


# Example list
my_list = [i for i in range(1001)]

# Shuffle the list
shuffled = shuffle_list(my_list)
print("Original list:", my_list)
print("Shuffled list:", shuffled)

with open("test-list.txt", "w") as f:
    f.write(f"{shuffled}")
