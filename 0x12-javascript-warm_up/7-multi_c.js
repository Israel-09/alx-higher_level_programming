#!/usr/bin/node
import { argv } from 'node:process';

const x = Number(argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
