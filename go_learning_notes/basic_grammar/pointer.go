package main

import "fmt"

func main(){
	i := 10
	p := &i

	fmt.Println(p)
	fmt.Println(*p)
	*p = 20
	fmt.Println(p)
	fmt.Println(*p)
	fmt.Println(i)
	fmt.Println(&i)
}