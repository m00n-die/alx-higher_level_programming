#!/usr/bin/node
// gets html content of a webpage

const url = process.argv[2];
const filepath = process.argv[3];

const fs = require('fs');
const request = require('request');

request.get(url, function (error, response, body) {
  // console.log(body)
  console.log(body);
  const stream = fs.createWriteStream(filepath, { encoding: 'utf-8' });
  stream.write(body);
  stream.end();
  if (error) {
    console.error(error);
  }
});
