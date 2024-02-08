#include <iostream>

void bubble_sort(int *arr, int arr_len) {
  for (int i = 0; i < arr_len - 1; i++) {
    for (int j = 0; j < arr_len - i - 1; j++) {
      if (arr[j] < arr[j + 1]) {
        // do nothing
      } else {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

int main() {

  int test_array[10] = {9, 5, 3, 7, 2, 8, 4, 1, 6, 0};

  std::cout << "unsorted:\n";
  for (int i : test_array) {
    std::cout << i << " ";
  }
  std::cout << "\n";

  int test_array_len = 0;
  for (int i : test_array) {
    test_array_len++;
  }

  bubble_sort(test_array, test_array_len);

  std::cout << "sorted:\n";
  for (int i : test_array) {
    std::cout << i << " ";
  }

  return 0;
}
