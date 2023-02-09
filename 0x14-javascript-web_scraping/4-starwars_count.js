#!/usr/bin/node

const request = require('request');
let count = 0;

request(`${process.argv[2]}`, (err, response, body) => {
  body = JSON.parse(body);
  if (err) { console.log(err); } else {
    for (const i in body.results) {
      count = body.results[i].characters.filter((ele) => {
        return ele.endsWith('people/18/');
      });
    }
  }
  console.log(count.length);
});
