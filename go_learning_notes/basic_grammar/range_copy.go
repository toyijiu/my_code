package main

var a = [3]int{0,1,2}


func main(){
	a := [3]int{0,1,2}
	println(&a[0],&a[1],&a[2])

	for i,v:= range a{
		println("new address:",&a[i],v)
		if i == 0{
			a[1],a[2] = 999,999
			println("cur address:",a[1],a[2],&a[1],&a[2])
		}

		a[i] = a[i]+100
		println("add address:",&a[i],a[i])
	}

	println("final value:",a[0],a[1],a[2])
}