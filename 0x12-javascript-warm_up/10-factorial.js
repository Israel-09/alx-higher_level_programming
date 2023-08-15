#!/usr/bin/node

function factorial (n) {
  if (n === 1 || isNaN(n) || n === 0) {
    return 1;
  }
  return (n + factorial(n - 1));
}

const n = Number(process.argv[2]);
console.log(factorial(n));
