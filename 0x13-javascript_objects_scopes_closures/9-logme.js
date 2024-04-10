#!/usr/bin/node
// MINE.
let num = 0; // Here num has a module scope.
exports.logMe = function (item) { // logMe creates a closure , by maintaining ref. to the num variable
  console.log(num + ': ' + item); // even after returning.
  num += 1; // this value of num is 'remembered' even after returning the function
};
