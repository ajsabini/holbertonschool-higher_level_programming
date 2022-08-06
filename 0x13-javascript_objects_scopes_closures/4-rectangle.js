#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    const x = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }

  rotate () {
    const rot = this.height;
    this.height = this.width;
    this.width = rot;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
