package main

import "fmt"

type Point struct{
	x int
	y int
}

func main(){
	point := Point{}
	point.x = 1
	point.y = 2

	p := &point
	fmt.Println(point)
	fmt.Println(&point)
	fmt.Println(p)
	fmt.Println(*p)

	p.x = 4
	p.y = 5
	fmt.Println(point)
	fmt.Println(&point)
	fmt.Println(p)
	fmt.Println(*p)
}