#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || !w || !h)) { // This ensures both arguments are undefined if w or h don't exist; or either is <= 0
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
