package main

import "fmt"

func main() {
	fmt.Printf("%d", getSum(1, 2))
}
func getSum(a, b int) int {
	if b == 0 {
		return a
	}
	var abor int = a ^ b
	var aband int = a & b
	return getSum(abor, aband<<1)
}
