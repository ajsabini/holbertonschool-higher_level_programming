#!/usr/bin/node

const uno = parseInt(process.argv[2], 10);
const dos = parseInt(process.argv[3], 10);

function add (x, y) {
  return (x + y);
}

console.log(add(uno, dos));
