#!/usr/bin/node
// prints the title of the movie for a given id

const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
const url = endpoint + process.argv[2];

request(url, function (error, response, body) {
  const jsonBody = JSON.parse(body);
  const movieTitle = jsonBody.title;
  console.log(movieTitle);
  if (error) {
    console.error(error);
  }
});
