#!/usr/bin/node

function PrintC (arg) {
  // Use Number() to attempt conversion with explicit checking for NaN
  const convert = Number(arg); /* Better than parseint() that only converts portion of string
                                to an integer, stopping at 1st non-numeric xter */
  let i = 0;
  if (Number.isNaN(convert)) {
    console.log('Missing number of occurrences');
  } else {
    while (i < convert) {
      console.log('C is fun');
      i++;
    }
  }
}
// Example usage:
const argv = process.argv;
PrintC(argv[2]);
