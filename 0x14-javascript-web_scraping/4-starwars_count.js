#!/usr/bin/node
// print number of movies where character is present

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (!error) {
    const struct = JSON.parse(body).struct;
    console.log(struct.reduce((count, chars) => {
      return chars.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  } else { console.log(error); }
});
