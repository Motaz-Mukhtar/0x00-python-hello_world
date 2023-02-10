#!/usr/bin/node

const request = require('request');
const count = [];

request(`${process.argv[2]}`, (err, response, body) => {
  body = JSON.parse(body);
  if (err) { console.log(err); } else {
    for (const i in body.results) {
      body.results[i].characters.filter((ele) => {
        return ele.endsWith('/people/18/') ? count.push(ele) : null;
      });
    }
  }
  console.log(count.length);
});
