package main

import "fmt"

type Point struct{
	x int
	y int
}

func main(){
	point := Point{1,2}
	fmt.Println(point)
	point.x = 3
	fmt.Println(point)
}