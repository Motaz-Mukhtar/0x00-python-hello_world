#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, response, body) => {
  const filmCharacters = [];
  if (err) { console.log(err); } else {
    JSON.parse(body).characters.forEach((ele) => {
      filmCharacters.push(ele);
    });
    filmCharacters.forEach((ele) => {
      request(ele, (err, response, body) => {
        if (err) { console.log(err); } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
