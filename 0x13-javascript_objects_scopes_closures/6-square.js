#!/usr/bin/node
const FirstSquare = require('./5-square');

class Square extends FirstSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log((c) ? c.repeat(this.width) : 'X'.repeat(this.width));
    }
  }
}

module.exports = Square;
