//unsafe指针可以和任意类型的指针转换
package main

import "unsafe"
import "fmt"
func main(){
	x := 0x12345678
	p := unsafe.Pointer(&x)
	n := (*[4]byte)(p)

	for i:=0;i<len(n);i++{
		fmt.Printf("%X\n",n[i])
	}
}