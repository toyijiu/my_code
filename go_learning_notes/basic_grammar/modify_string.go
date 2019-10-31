package main


func main(){
	test_str := "abcd"
	uni_str := []rune(test_str)
	uni_str[1] = 'B'
	println(string(uni_str))
}