#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method
  print () {
    let x = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }
      if (i < this.height - 1) { x += '\n'; }
    }
    console.log(x);
  }

  // Method
  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  // Method
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
