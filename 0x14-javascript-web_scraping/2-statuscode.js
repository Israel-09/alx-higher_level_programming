#!/usr/bin/node
// output the status code from a request to a url

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  console.log('code:', response.statusCode);
  if (error) {
    console.error(error);
  }
});
