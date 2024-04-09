#!/usr/bin/node
// MINE
class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || !w || !h)) { // This ensures both arguments are undefined if w or h don't exist; or either is <= 0
      this.width = w; // This doesn't create an empty object, but if the condition is not met, it doesnt init any value for
      this.height = h; // w, h passed. They come out as undefined, and the class prints out no argument.
    }
  }

  print () { // HERE USE DATA FIELDS (width, height) not (w,h)
    let i = 0;
    let j = 0;
    const array = new Array(this.height); // create a new array
    while (i < this.height) {
      array[i] = new Array(this.width); // create a new array for every element of the array - 2D
      while (j < this.width) {
        array[i].push('X'); // array property to push in an element
        j++;
      } // j = convert
      j = 0; // Reassign j to 0.
      i++;
    }
    for (i = 0; i < this.height; i++) { // print every element in a sub array , together as a string separated by ""
      console.log(array[i].join(''));
    }
  }
}
module.exports = Rectangle;
