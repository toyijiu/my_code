package main

func add(x,y int) (z int){
	defer func(){
		println("begin to add 100")
		z += 100
	}()

	z = x + y
	println("cur value:",z)
	return
}

func main(){
	println(add(1,2))
}