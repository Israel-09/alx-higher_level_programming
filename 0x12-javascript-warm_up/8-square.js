#!/usr/bin/node

const size = process.argv[2];

if (parseInt(size)) {
  for (let i = 0; i < size; i++) {
    let str = '';
    let j = 0;

    while (j < size) {
      str = str + 'X';
      j++;
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
