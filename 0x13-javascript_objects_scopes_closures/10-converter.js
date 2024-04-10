#!/usr/bin/node
// MINE
exports.converter = function (base) {
  return number => (number.toString(base).toUpperCase()); // an inner function to accept a parameter (number)
  // to return the number in provided base
};
