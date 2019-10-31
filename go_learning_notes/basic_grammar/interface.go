package main

import(
	"fmt"
	"math"
)

type MyFloat float64
func (f MyFloat) Abs() float64{
	if f < 0{
		return float64(-f)
	}else{
		return float64(f)
	}
}

type Vertex struct{
	x,y float64
}

func (v *Vertex) Abs() float64{
	return math.Sqrt(v.x*v.x + v.y*v.y)
}

type Abser interface{
	Abs() float64
}

func main(){
	var my_if Abser
	my_f := MyFloat(-math.Sqrt2)
	my_v := Vertex{3,4}

	my_if = &my_v
	my_if = my_f
	

	

	fmt.Println(my_if.Abs())

}