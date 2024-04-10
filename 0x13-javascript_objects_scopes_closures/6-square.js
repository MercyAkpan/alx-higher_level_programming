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
    }
  }
}
module.exports = Square;
