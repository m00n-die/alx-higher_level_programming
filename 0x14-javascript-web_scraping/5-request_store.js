#!/usr/bin/node
// gets html content of a webpage

let url = process.argv[2];
let filepath = process.argv[3];

const fs = require('fs').promises;
const request = require('request');

request.get(url, function (error, response, body) {
        console.log(body)
        .pipe(fs.createWriteStream(filepath))
        };
