const fs = require('fs');

const readAndPrintFile = (filePath) => {
  try {
    // Read the file synchronously with utf-8 encoding
    const data = fs.readFileSync(filePath, 'utf-8');

    try {
      // Try to parse the text as JSON
      const jsonData = JSON.parse(data);
      // Pretty print the JSON data
      console.log(JSON.stringify(jsonData, null, 4));
    } catch (jsonError) {
      // If parsing fails, it is not JSON, so print the raw text
      console.log(data);
    }
  } catch (error) {
    // Print the error object if an error occurred during reading the file
    console.error('An error occurred:', error);
  }
};

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <file_path>');
} else {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
}
