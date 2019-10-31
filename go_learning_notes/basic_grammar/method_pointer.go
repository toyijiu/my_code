package main

import "fmt" 
import "math"

type Vertex struct{
	x,y float64
}

func (v *Vertex) Scale(times float64){
	v.x = v.x*times
	v.y = v.y*times
}

func (v *Vertex) Abs() float64{
	return math.Sqrt(v.x*v.x + v.y*v.y)
}

func main(){
	p := &Vertex{2,3}
	q := Vertex{2,3}
	fmt.Println(p.Abs())
	p.Scale(10)
	q.Scale(10)
	fmt.Println(*p)
	fmt.Println(q)
}