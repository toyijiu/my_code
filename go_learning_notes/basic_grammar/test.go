package main

var s string
//枚举，iota表示从0开始
const(
	Sunday = iota
	Monday
	Tuesday
	Wednesday
	Thursday
)
const(
	aa = "abc"
	bb	//bb = "abc"
)
func main(){
	//局部常量可以只定义不使用，局部变量则不行
	const x = "xxx"
	println(bb)
	s := "abc"
	println(&s)

	//和上面的s 在同一个域，不重新定义
	s,y := "hello",20
	println(&s,y)
	{
		//和上面的s在不同域，重新定义内存空间
		s,z := "world",30
		println(&s,z)
	}
}