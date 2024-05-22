#!/usr/bin/node
const { exec } = require('child_process');

// URL to fetch
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <url>') 
} else {
const url = process.argv[3] 
}
const url = "www.mercyakpan.tech" 

// Execute curl command to get status code
exec(`curl -s -o /dev/null -I -w "%{http_code}" ${url}`, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Error: ${stderr}`);
    return;
  }
  // Print status code in the desired format
  console.log(`Code: ${stdout}`);
});

