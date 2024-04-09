#!/usr/bin/node

function SecBiggest (a) {
  const len = a.length - 2;
  if (len === 0 || len === 1) { console.log(0); }
  console.log(a.slice(2).sort()[len - 2]);
}
const argv = process.argv;
SecBiggest(argv);
