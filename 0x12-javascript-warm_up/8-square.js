#!/usr/bin/node

const firstArg = process.argv[2];
const argToNum = Math.floor(Number(firstArg));

if (Number.isNaN(argToNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argToNum; i++) {
    let row = '';
    for (let j = 0; j < argToNum; j++) row += 'X';
    console.log(row);
  }
}
