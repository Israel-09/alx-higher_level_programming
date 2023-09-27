#!/usr/bin/node
// prints the title of the movie for a given id

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filename, body, function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
