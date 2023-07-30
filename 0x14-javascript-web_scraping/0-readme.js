#!/usr/bin/node
// reads a file

const filename = (process.argv[2]).toString();
const fs = require('fs').promises;
async function readFile (fileName) {
  try {
    const content = await fs.readFile(fileName, { encoding: 'utf-8' });
    console.log(content.toString());
  } catch (error) {
    console.error(error);
  }
}

readFile(filename);
