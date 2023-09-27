#!/usr/bin/node
// write a text to a provided file

const file = process.argv[2];
const text = process.argv[3];

const fs = require('fs');

fs.writeFile(file, text,
  function (err) {
    if (err) {
      return console.error(err);
    }
  });
