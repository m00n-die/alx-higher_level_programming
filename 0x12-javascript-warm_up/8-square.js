#!/usr/bin/node

const firstArg = process.argv[2];
const argToNum = Math.floor(Number(firstArg));

if (Number.isNaN(argToNum)) {
  console.log('Missing size');
}

for (let i = 0; i < argToNum; i++) {
  for (let j = 0; j < argToNum; j++) {
  console.log('X');
  console.log(' ');
}
}
