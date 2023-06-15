#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if ((this.width === 0 || this.width < 0) || (this.height === 0 || this.height < 0)) {
      const empty = new Rectangle();
      return empty;
    }
  }
}
