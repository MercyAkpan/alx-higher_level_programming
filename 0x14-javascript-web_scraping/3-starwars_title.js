#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
// console.log(film_id)
// Request URL
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
// console.log(url)
request(url, { json: true }, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(error);

  // Printing status code
  // console.log(response.statusCode);

  // Printing body
  const trial = body;
  console.log(trial.title);
});
