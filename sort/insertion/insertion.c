#include <stdio.h>

void insertion_sort(int *arr, int length) {
  /* passes by reference so no return is needed */
  /* changes array as needed and the array will be modified outside this proc */

  for (int i = 0; i < length; i++) {
    int current_value = arr[i];
    if (current_value > arr[i - 1]) {
      ;
    } else {
      while (current_value < arr[i - 1] && i > 0) {
        arr[i] = arr[i - 1];
        i = i - 1;
      }
      arr[i] = current_value;
    }
  }
}

int main() {
  // 10 is being extra specific on how many elements there are in the array
  // can help with readability on large arrays, only have to look at the num
  int test_array[10] = {9, 5, 3, 7, 2, 8, 4, 1, 6, 0};

  // size_t is actually just an unsigned long
  size_t test_array_len = sizeof(test_array) / sizeof(test_array[0]);

  printf("unsorted:\n");
  for (int i = 0; i < test_array_len; i++) {
    printf("%d ", test_array[i]);
  }

  printf("\nsorted:\n");

  // don't need to pass &test_array here
  // because binary_search() expects a pointer to the first element of the
  // array which is what is passed here, with just `test_array`. no baggage.

  // if `&test_array` is passed, binary_search() would receive the address of
  // the entire array,
  // which would lead to incorrect behaviour -> a logic error
  // (colloquially named a runtime error outside of OCR land)

  // theory: you only need to pass the address of the first element
  // because arrays are stored in contiguous space in memory,
  // meaning that the compiler can work out where the rest of the elements
  // are
  insertion_sort(test_array, test_array_len);

  for (int i = 0; i < test_array_len; i++) {
    printf("%d ", test_array[i]);
  }

  return 0;
}
