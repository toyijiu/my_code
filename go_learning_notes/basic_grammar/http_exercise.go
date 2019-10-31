package main

import(
	"log"
	"net/http"
	"fmt"
)

type String string

type Struct struct{
	Greeting String
	Punct string
	Who	string
}

func (str String) ServeHTTP(w http.ResponseWriter,r *http.Request){
	fmt.Fprint(w,str)
}
func (stru Struct) ServeHTTP(w http.ResponseWriter,r *http.Request){
	fmt.Fprint(w,stru)
}

func main(){
	http.Handle("/string", String("I'm a frayed knot."))
	http.Handle("/struct", &Struct{"Hello", ":", "Gophers!"})
	log.Fatal(http.ListenAndServe("localhost:8080", nil))
}