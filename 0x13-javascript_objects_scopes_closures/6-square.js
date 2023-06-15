#!/usr/bin/node

const squareClass = require('./5-square');

class Square extends squareClass {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let shape = '';
      for (let j = 0; j < this.width; j++) {
        shape += c;
      }
      console.log(shape);
    }
  }
}

module.exports = Square;
