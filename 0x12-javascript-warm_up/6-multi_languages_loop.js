#!/usr/bin/node
// :n <name of file> , to switch to new file
const strings = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0; // i changes, so not a const
while (i < strings.length) {
  console.log(strings[i]);
  i++;
}
