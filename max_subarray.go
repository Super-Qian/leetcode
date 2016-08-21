package main

import "fmt"

func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	n := maxSubArray(nums)
	fmt.Printf("%d\n", n)
}

func maxSubArray(nums []int) int {
	sum := nums[0]
	num := nums[0]
	for i := 1; i < len(nums); i++ {
		if num < 0 {
			num = nums[i]
		} else {
			num += nums[i]
		}
		if sum < num {
			sum = num
		}
	}
	return sum
}
