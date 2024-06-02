#!/usr/bin/node
const request = require('request');
// This is the filmId of the movie. 
const filmId = process.argv[2];
// Request URL
const url = `${filmId}`
//console.log(url)
// Getting the url, error, response, body
// Without this json:true, the response wont be parse as JSON string
// for easy data retrieval.
request(url, { json: true }, (error, response, body) => {
  // Printing the error if occurred
//  if (error) console.log(error);
  // Printing status code
  // console.log(response.statusCode);

  // Printing body
//  console.log(body.results[0].characters);
//  characters = body.results[0].characters
  characters = body.results[0].characters.map(character => character.toString());
//  console.log(characters)
  userId = 18
  const trial = `https://swapi-api.alx-tools.com/api/people/${userId}/`
//  console.log(trial)
  if (characters.includes(trial)) {
//    console.log("here")
  }  else {
//  console.log("not here");
}
const trial2 = `https://swapi-api.alx-tools.com/api/people/${userId}/`
request(trial2, { json: true }, (error, response, body) => {
    console.log(body.films.length) 
});
});
