#!/usr/bin/node
// prints the title of the movie for a given id

const request = require('request');

const endpoint = process.argv[2];
const userUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(endpoint, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jsonBody = JSON.parse(body);
    const results = jsonBody.results;
    let count = 0;
    for (const result of results) {
      const characters = result.characters;

      if (characters.includes(userUrl)) {
        count++;
      }
    }
    console.log(count);
  }
}
);
