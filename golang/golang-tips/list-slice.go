package main

import "fmt"

//list slicing
func main() {
    fruits := [6]string{"apple", "orange", "mango", "banana", "pear","berry"}

	var s []string = fruits[1:4]
	fmt.Println(s) //[orange mango banana]
}
