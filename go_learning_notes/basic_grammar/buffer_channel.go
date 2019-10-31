package main

import "fmt"

func main(){
	c := make(chan int,100)


	for i:=0;i<100;i++{
		c<-i
		fmt.Println("成功入队:",i)
	}
	for  i:=0;i<100;i++{
		fmt.Println(<-c)
	}

}