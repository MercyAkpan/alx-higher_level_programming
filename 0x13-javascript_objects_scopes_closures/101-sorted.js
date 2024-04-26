#!/usr/bin/node
// This takes a dictionary , and fromats it into a new dictionary , based on number of occurences 
// of each key.
//const fs = require('fs');
//const data = fs.readFileSync('./101-data.js', 'utf8');
//const jsonData = JSON.parse(data.replace(/^(module\.exports = )?(.*)$/, '')); // Capture the value (optional leading whitespace)
//const { dict } = jsonData; // Access the 'dict' property
const dict1 = require('./101-data.js').dict;
console.log(dict1);
const dict2 = {};
for (const [key, value] of Object.entries(dict1)) { // Object.entries is used to destructure dictionaries well in JS.
  if (dict2[value]) {
    dict2[value].push(key);
  } else {
    dict2[value] = [key];
  }
}
console.log(dict2);
// const formattedDict = Object.entries(originalDict).map(([key, value]) => ({
//  [key]: (key === "age" && value >= minAge) ? "Eligible" : value
// }));
