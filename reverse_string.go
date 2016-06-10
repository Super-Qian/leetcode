package main

import (
	"fmt"
	//"time"
)

func main() {
	//starttime := time.Now()
	s := "hello，golang"
	fmt.Println(reverseString(s))
	//fmt.Println(time.Now().Sub(starttime))
	//fmt.Println(reverseString(reverseString(s)))
}

func reverseString(s string) string {
	runes := []rune(s)
	for from, to := 0, len(runes)-1; from < to; from, to = from+1, to-1 {
		runes[from], runes[to] = runes[to], runes[from]
	}
	return string(runes)
}
