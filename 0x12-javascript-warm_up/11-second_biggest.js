#!/usr/bin/node

function SecBiggest (a) {
  let i = 0;
  const b = a.slice(2);
  const len = b.length;
  if (len === 0 || len === 1) {
    console.log(0);
    return;
  }
  while (i < len) {
    b[i] = Number(b[i]);
    i++;
  }
  const sortedNumbers = b.sort((a, j) => a - j);
  console.log(sortedNumbers[sortedNumbers.length - 2]);
//  console.log((b.sort()[len - 2]));
}
const argv = process.argv;
SecBiggest(argv);
