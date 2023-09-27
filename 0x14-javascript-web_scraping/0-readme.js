#!/usr/bin/node
// write a text to the provided file in ARGV[1]

const arg1 = process.argv[2];

const fs = require('fs');

fs.readFile(arg1, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
