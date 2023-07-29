#!/usr/bin/node
// writes to a file

const file_path = (process.argv[2]).toString();
const stringToWrite = process.argv[3];

const fs = require('fs').promises;
async function writeToFile (filePath, content) {
  try {
    const newContent = content;
    await fs.writeFile(filePath, newContent);
  } catch (error) {
    console.error(error);
  }
}

writeToFile(file_path, stringToWrite);
