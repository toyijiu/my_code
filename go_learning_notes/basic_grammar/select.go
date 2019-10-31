package main

import "fmt"

func fibonacci(c,quit chan int){
	x,y:=0,1
	for{
		select{
		case c<-x:
			x,y = y,x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func operation(c,quit chan int){
	for i:=0;i<10;i++{
		fmt.Println(<-c)
	}
	quit<-0
}
func main(){
	c := make(chan int)
	quit := make(chan int)

	go operation(c,quit)

	fibonacci(c,quit)
}