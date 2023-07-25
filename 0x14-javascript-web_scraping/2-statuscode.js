#!/usr/bin/node
// send a get request

let firstArg = process.argv[2];

const request = require('request');
request.get(firstArg, function (error, response, body) {
    console.log('code: ', response && response.statusCode);
    });
