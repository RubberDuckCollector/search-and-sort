#include <iostream>
#include <vector>

std::vector<int> insertion_sort(std::vector<int> l) {

  for (int i = 1; i < l.size(); i++) {
    int current_value = l[i];

    if (current_value > l[i - 1]) {
      ;
    } else {
      while (i > 0 && current_value < l[i - 1]) {
        l[i] = l[i - 1];
        i = i - 1;
      }
      l[i] = current_value;
    }
  }

  std::vector<int> sorted_vector = l;

  return sorted_vector;
}

int main() {
  std::vector<int> test_vector = {9, 5, 3, 7, 2, 8, 4, 1, 6, 0};

  std::cout << "Original vector:";
  for (int i = 0; i < test_vector.size(); i++) {
    std::cout << " " << test_vector[i];
  }
  std::cout << std::endl;

  std::vector<int> sorted_vector = insertion_sort(test_vector);

  std::cout << "Sorted vector:";
  for (int i = 0; i < sorted_vector.size(); i++) {
    std::cout << " " << sorted_vector[i];
  }
  std::cout << std::endl;
  return 0;
}
