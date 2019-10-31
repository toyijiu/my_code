package main

import "fmt"

func Sqrt(x float64) float64{
	z := 1.0
	for i:=0;i<10;i++{
		z = z - (z*z-x)/2/z
		fmt.Printf("the %d times result:%f\n",(i+1),z)
	}
	return z
}

func main(){
	var result float64 = Sqrt(2)
	fmt.Println(result)
}