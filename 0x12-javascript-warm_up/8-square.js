#!/usr/bin/node

function MakeaSquare (arg) {
  // Use Number() to attempt conversion with explicit checking for NaN
  const convert = Number(arg); /* Better than parseint() that only converts portion of string
                                to an integer, stopping at 1st non-numeric xter */
  if (Number.isNaN(convert)) {
    console.log('Missing number of occurrences');
  } else {
    try { // For positive values
      let i = 0; let j = 0; const array = new Array(convert); // create a new array
      while (i < convert) {
        array[i] = new Array(convert); // create a new array for every element of the array - 2D
        while (j < convert) {
          array[i].push('X'); // array property to push in an element
          j++;
        } // j = convert
        j = 0; // Reassign j to 0.
        i++;
      }
      for (i = 0; i < convert; i++) { // print every element in a sub array , together as a string separated by ""
        console.log(array[i].join(''));
      }
    } catch (error) { // for negative elements
    }
  }
}
// Example usage:
const argv = process.argv;
MakeaSquare(argv[2]);
