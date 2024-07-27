package main

import (
	"fmt"
)

func binarySearch(arr []int, target int) int {
	leftPointer := 0
	rightPointer := len(arr) - 1
	midpoint := leftPointer + (rightPointer-leftPointer)/2

	for leftPointer <= rightPointer {
		if arr[midpoint] == target {
			return midpoint
		} else if arr[midpoint] < target {
			leftPointer = midpoint + 1
		} else {
			rightPointer = midpoint - 1
		}
	}
	return -1
}

func main() {
	myArray := []int{1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10}

	fmt.Println(myArray)

	fmt.Println("binary search")
	for i := range myArray {
		fmt.Printf("binary search of %d: %d\n", myArray[i], binarySearch(myArray, myArray[i]))
	}

}
