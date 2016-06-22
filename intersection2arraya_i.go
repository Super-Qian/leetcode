package main

import "fmt"

func main() {
	nums1 := []int{1, 2, 2, 1, 4, 3}
	nums2 := []int{2, 3}
	a := []int{nums2[0]}
	for _, num := range nums1 {
		for _, num2 := range nums2 {
			if num == num2 {
				for _, anum := range a {
					if anum != num {
						a = append(a, num)
					}
				}
			}
		}
	}
	fmt.Println(a)
}
