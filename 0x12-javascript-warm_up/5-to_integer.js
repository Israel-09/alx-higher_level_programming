#!/usr/bin/node

let x = process.argv[2];

if (parseInt(x)) {
  console.log(`My number: ${x}`);
} else {
  console.log('Not a number');
}
