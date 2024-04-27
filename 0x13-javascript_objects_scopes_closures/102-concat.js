#!/usr/bin/node
const args = process.argv;
try {
  const fs = require('fs');
  const file1 = fs.readFileSync(args[2], 'utf8'); // To read a file from command line argument.
  const file2 = fs.readFileSync(args[3], 'utf8');
  const file3 = file1 + file2;
  fs.writeFileSync('file3', file3, 'utf8');
  console.log(file3);
} catch (error) {
  console.error('Nope');
}
