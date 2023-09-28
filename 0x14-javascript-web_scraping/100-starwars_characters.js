#!/usr/bin/node
// prints the title of the movie for a given id

const request = require('request');
const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
const url = endpoint + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
          return;
        }
        const characterDetails = JSON.parse(body);
        console.log(characterDetails.name);
      });
    }
  }
});
