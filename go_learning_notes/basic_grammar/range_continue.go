package main

import "fmt"

func main(){
	list := make([]int,10)
	for i,_ := range list{
		list[i] = 1 << uint(i)
	}
	for _,value := range list{
		fmt.Println(value)
	}
}