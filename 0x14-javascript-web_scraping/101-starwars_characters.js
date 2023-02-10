#!/usr/bin/node

const request = require('request');

function printCharacters (arr, index) {
  request(arr[index], (err, response, body) => {
    if (err) { console.log(err); } else {
      console.log(JSON.parse(body).name);
      if (index === arr.length - 1) { return (0); } else {
        printCharacters(arr, index + 1);
      }
    }
  });
}

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, response, body) => {
  if (err) { console.log(err); } else {
    const arr = JSON.parse(body).characters;
    printCharacters(arr, 0);
  }
});
