#!/usr/bin/node
const fs = require('fs');

const writeToFile = (filePath, content) => {
  try {
    // Write the content to the file synchronously with UTF-8 encoding
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log('File written successfully.');
  } catch (error) {
    // Print the error object if an error occurred during writing
    console.error('An error occurred:', error);
  }
};

if (process.argv.length !== 4) {
  console.log('Usage: node script.js <file_path> <content>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeToFile(filePath, content);
}
