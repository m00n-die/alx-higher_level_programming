#!/usr/bin/node

const firstArg = process.argv[2];
const secondArg = process.argv[3];

function add (a, b) {
  a = Math.floor(Number(firstArg));
  b = Math.floor(Number(secondArg));
  console.log(a + b);
}
