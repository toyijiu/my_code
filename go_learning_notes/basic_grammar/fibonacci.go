package main

import "fmt"

func fibonacci() func() int{
	pre := 0
	later := 0
	sum := 1
	return func()int{
		pre = later
		later = sum
		sum = pre + later
		return sum
	}

}

func main(){
	fib := fibonacci()
	for i:=0;i<10;i++{
		fmt.Println(fib())
	}
}