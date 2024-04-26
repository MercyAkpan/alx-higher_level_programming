#!/usr/bin/node
const dict1 = require('./101-data.js').dict;
console.log(dict1);
const dict2 = {};
for (const [key, value] of Object.entries(dict1)) {
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
