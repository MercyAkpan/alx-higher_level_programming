#!/usr/bin/node

function add (a, b) {
  if (!a || !b) {
    console.log('NaN');
    return;
  }
  console.log(a + b);
}
const argv = process.argv;
add(parseInt(argv[2]), parseInt(argv[3]));
