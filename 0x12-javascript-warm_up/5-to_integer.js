#!/usr/bin/node

const firstArg = process.argv[2];
const argToNum = Math.floor(Number(firstArg));

if (Number.isNaN(argToNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argToNum);
}
