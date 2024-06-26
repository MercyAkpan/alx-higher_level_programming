#!/usr/bin/node

function ToInteger (arg) {
  // Use Number() to attempt conversion with explicit checking for NaN
  const convert = Number(arg); /* Better than parseint() that only converts portion of string
                                to an integer, stopping at 1st non-numeric xter */
  if (Number.isNaN(convert)) {
    console.log('Not a number');
  } else {
    // If it's a valid integer, proceed with your logic using converted
    console.log('My number:', convert); // Example usage
  }
}

// Example usage:
const argv = process.argv;
ToInteger(argv[2]); // Output: "Not a number"
