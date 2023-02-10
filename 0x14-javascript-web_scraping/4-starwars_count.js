#!/usr/bin/node

const request = require('request');
const count = [];
const charaUrl = 'https://swapi-api.alx-tools.com/api/people/18';

request(`${process.argv[2]}`, (err, response, body) => {
  body = JSON.parse(body);
  if (err) { console.log(err); } else {
    for (const i in body.results) {
      body.results[i].characters.filter((ele) => {
        return ele === charaUrl ? count.push(ele) : null;
      });
    }
  }
  console.log(count.length);
});
