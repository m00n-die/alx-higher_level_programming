#!/usr/bin/node

const firstArg = process.argv[2];
const argToNum = Math.floor(Number(firstArg));
let i = 0;

if (Number.isNaN(argToNum)) {
  console.log('Missing number of occurrences');
} else {
  while (i < argToNum) {
    console.log('C is fun');
    i++;
  }
}
