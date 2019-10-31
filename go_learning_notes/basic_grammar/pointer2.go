package main
import "fmt"
type Data struct{
	a int
}

func main(){
	data := Data{1234}
	p := &data
	fmt.Printf("%T,%p,%v",p,p,p.a)

}