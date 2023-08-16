#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  return sum;
}

const a = process.argv[2];
const b = process.argv[3];

const sum = add(parseInt(a), parseInt(b));
console.log(sum);
