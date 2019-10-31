package main

import(
	"fmt"
	"log"
	"net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP(w http.ResponseWriter,r *http.Request){
	fmt.Fprint(w,"hello wuxiao!")
}

func main(){
	var h Hello
	fmt.Printf("begin to listen the port 8080\n")
	err := http.ListenAndServe("localhost:8080",h)
	fmt.Printf("Something comes in\n")
	if err != nil{
		log.Fatal(err)
	}
}