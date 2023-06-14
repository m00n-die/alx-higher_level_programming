#!/usr/bin/node

const firstArg = process.argv[2];
const firstInt = Math.floor(Number(firstArg));

function factorial (num) {
  if (num.isNaN() || num === 0 || num === 1) {
    return 1;
  } else if (!num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(firstInt));
