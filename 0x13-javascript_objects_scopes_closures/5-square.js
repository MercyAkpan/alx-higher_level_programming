#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) { // Takes in size as argument
    super(size, size); // w, h in Super is size
  }
}
module.exports = Square;
