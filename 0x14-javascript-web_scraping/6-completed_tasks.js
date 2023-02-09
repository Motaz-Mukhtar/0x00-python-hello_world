#!/usr/bin/node

const request = require('request');
let count = 1;
const tasksObject = {};

request('process.argv[2]', (err, response, body) => {
  if (err) { console.log(err); } else {
    const arr = JSON.parse(body).filter((ele) => {
      return ele.completed === true ? ele : null;
    });

    for (const i in arr) {
      tasksObject[`${count}`] = arr[i].userId;
      count++;
    }
  }
  console.log(tasksObject);
});
