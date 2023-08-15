#!/usr/bin/node

const x = process.argv[2];

if (parseInt(x)) {
  console.log(`My number: ${x}`);
} else {
  console.log('Not a number');
}
