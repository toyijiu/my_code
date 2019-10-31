package main

import(
	"fmt"
	"time"
)

func main(){
	cur_time := time.Now()
	switch  {
	case cur_time.Hour() < 12:
		fmt.Printf("Good morning")
	case cur_time.Hour() < 18:
		fmt.Printf("Good afternoon")
	default:
		fmt.Printf("Good evening")
		
	}
}