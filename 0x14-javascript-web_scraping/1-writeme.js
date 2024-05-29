#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of arguments are provided
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file
fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    // Print the error object if an error occurred during writing
    console.error(error);
  }
});
