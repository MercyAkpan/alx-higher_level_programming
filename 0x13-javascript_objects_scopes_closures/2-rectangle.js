#!/usr/bin/node
// MINE
class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || !w || !h)) { // This ensures both arguments are undefined if w or h don't exist; or either is <= 0
      this.width = w; // This doesn't create an empty object, but if the condition is not met, it doesnt init any value for
      this.height = h; // w, h passed. They come out as undefined, and the class prints out no argument.
    }
  }
}
module.exports = Rectangle;
