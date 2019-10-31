package main

import "fmt"

type Vertex struct{
	x,y int
}




func main(){
	cur_map := map[string]Vertex{
		"test":Vertex{1,2},
		"2":Vertex{3,4},
	}
	cur_map["test"] = Vertex{1,2}
	fmt.Println(cur_map["2"])
}