#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1) {
  if (arg2) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
