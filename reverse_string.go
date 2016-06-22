package main

import (
	"fmt"
	//"time"
	"bufio"
	"os"
	"strings"
)

func main() {
	//starttime := time.Now()
	input := bufio.NewReader(os.Stdin)
	r, _ := input.ReadString('\n')
	t := strings.TrimRight(r, "\n")
	fmt.Println("下面用的是scanf不能有空格")
	var a string
	fmt.Scanln(&a)
	s := "hello，golang"
	fmt.Println(reverseString(s))
	fmt.Println(reverseString(a))
	fmt.Println(reverseString(t))
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
