#!/usr/bin/node
//const { exec } = require('child_process');
//
//// URL to fetch
//const url = process.argv[2] 
////const url = "www.mercyakpan.tech" 
//
//// Execute curl command to get status code
//exec(`curl -s -o /dev/null -I -w "%{http_code}" ${url}`, (error, stdout, stderr) => {
//  if (error) {
//    console.error(`Error: ${error.message}`);
//    return;
//  }
//  if (stderr) {
//    console.error(`Error: ${stderr}`);
//    return;
//  }
//  // Print status code in the desired format
//  console.log(`Code: ${stdout}`);
//});
//
const request = require('request');

// Check if the URL argument is provided
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    // Print only the error object
    console.error(error);
  } else {
    // Print the status code in the required format
    console.log(`code: ${response.statusCode}`);
  }
});

