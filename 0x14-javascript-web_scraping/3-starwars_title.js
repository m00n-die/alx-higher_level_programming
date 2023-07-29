#!/usr/bin/node
// makes a getrequest to an api

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId

const request = require('request');
request.get(apiUrl, function (error, response, body) {
  if (!error) {
    let struct = JSON.parse(body);
    console.log(struct.title);
    } else
      console.log(error);
});
