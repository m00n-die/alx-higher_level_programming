#!/usr/bin/node

let filename = (process.argv[2]).toString();
const fs = require('fs').promises;
async function readFile(file_name) {
    try {
        const content = await fs.readFile(file_name);
        console.log(content.toString());
    } catch (error) {
        console.error(error);
    }
}

readFile(filename);
