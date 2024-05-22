const fs = require('fs');

// Check if the correct number of arguments are provided
if (process.argv.length !== 4) {
  console.log('Usage: node script.js <file_path> <content>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];

  // Write the content to the file
  fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) {
      // Print the error object if an error occurred during writing
      console.error('An error occurred:', error);
    } else {
      console.log(`Content successfully written to ${filePath}`);
    }
  });
}

