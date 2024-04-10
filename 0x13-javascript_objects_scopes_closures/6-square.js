#!/usr/bin/node
// MINE -- to comment out :s/^/\/\/
const vars = require('./5-square');

class Square extends vars { // here Square extends the class in const vars (=== Square) in ./5-square
// No constructor needed here, and default super(), is n default constructor
  charPrint (c) {
    this.c = c;
    if (!c) {
      this.print(); // same as this instance should access the print function in the Superclass
    } else {
		this.a = c // This access the superclass variable and define it as c. Not this.print().a = c DIDN'T WORK
		this.print() // This then acees the print variable with a = c.
//      let i = 0;
//      let j = 0;
//      try { // To catch RangeError for -ve numbers
//        const array = new Array(this.height); // create a new array
//        while (i < this.height) {
//          array[i] = new Array(this.width); // create a new array for every element of the array - 2D
//          while (j < this.width) {
//            array[i].push(this.c); // array property to push in an element
//            j++;
//          } // j = convert
//          j = 0; // Reassign j to 0.
//          i++;
//        }
//        for (i = 0; i < this.height; i++) { // print every element in a sub array , together as a string separated by ""
//          console.log(array[i].join(''));
//        }
//      } catch (RangeError) {
//      }
    }
  }
}
module.exports = Square;
