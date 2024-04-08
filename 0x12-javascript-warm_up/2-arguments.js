#!/usr/bin/node

const argv = process.argv.length; // This gets the length of the process.argv property(command- line arguments)
if (argv === 2) {
  console.log('No argument');
} else if (argv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
