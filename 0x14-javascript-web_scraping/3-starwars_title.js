#!/usr/bin/node
// Print the title of the Star Wars movie matching the given number
const url = `http://swapi.co/api/films/${process.argv[2]}`;
const request = require('request');
request(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (body) {
    console.log(body.title);
  }
});
