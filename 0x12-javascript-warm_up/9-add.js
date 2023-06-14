#!/usr/bin/node

const firstArg = process.argv[2];
const secondArg = process.argv[3];
const firstInt = Math.floor(Number(firstArg));
const secondInt = Math.floor(Number(secondArg));

function add (a, b) {
  return a + b;
}

console.log(add(firstInt, secondInt));
