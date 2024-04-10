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
    b[i] = Number(b[i]); // converts all elements to numbers
    i++;
  }
  const sortedNumbers = b.sort((a, j) => a - j); // an inbuilt function to sort (modifying) the b array
  console.log(sortedNumbers[sortedNumbers.length - 2]); // obtain 2nd to last index
//  console.log((b.sort()[len - 2])); // This sorts based on unicode: [1<10<11<3<5 not [1<3<5<10<11]
}
const argv = process.argv;
SecBiggest(argv);
