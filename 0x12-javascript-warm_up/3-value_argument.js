#!/usr/bin/node
// Ctrl- G to get name of file
const argv = process.argv; // This gets the process.argv property(command- line arguments)
if (!argv[2]) {
  console.log('No argument');
} else if (argv[2]) {
  console.log(argv[2]);
}
