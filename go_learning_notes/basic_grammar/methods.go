package main

import "fmt"
import "math"

type Vertex struct{
	x,y float64
}

func (v Vertex) abs() float64{
	return math.Sqrt(v.x*v.x + v.y*v.y)
}

func main(){
	p := Vertex{3.0,4.5}
	fmt.Println(p.abs())
}