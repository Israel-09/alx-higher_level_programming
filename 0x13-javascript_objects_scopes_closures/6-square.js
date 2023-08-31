#!/usr/bin/node
const old = require('./5-square');

class Square extends old {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let x = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c) { x += c; } else { x += 'X'; }
      }
      if (i < this.height - 1) { x += '\n'; }
    }
    console.log(x);
  }
}

module.exports = Square;
