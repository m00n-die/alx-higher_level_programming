#!/usr/bin/node
// reads a file

const filename = (process.argv[2]).toString();
const fs = require('fs').promises;
async function readFile (file_name) {
  try {
    const content = await fs.readFile(file_name, { encoding: 'utf-8' });
    console.log(content.toString());
  } catch (error) {
    console.error(error);
  }
}

readFile(filename);
