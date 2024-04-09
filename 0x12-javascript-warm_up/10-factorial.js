#!/usr/bin/node

function FacTorial (a) {
  if (!a || a === 0) {
    return (1); // for undefined and 0 values
  } else if (a === 1) {
    return (1);
  }
  return (a * (FacTorial(a - 1))); // return, each recursion, not print
}
const argv = process.argv;
console.log(FacTorial(parseInt(argv[2]))); // print entire result
