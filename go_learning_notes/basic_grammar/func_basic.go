package main
import "fmt"

func add(x int,y int) int{
	return x + y
}

func main(){
	c := add(1,2)
	fmt.Println(c)
}