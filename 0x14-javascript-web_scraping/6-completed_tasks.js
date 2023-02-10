#!/usr/bin/node

const request = require('request');

request(`${process.argv[2]}`, (err, response, body) => {
  if (err) { console.log(err); } else {
    let tasksObject = {};
    JSON.parse(body).forEach((ele) => {
      if (ele.completed && tasksObject[ele.userId] === undefined) {
        tasksObject[ele.userId] = 1;
      } else if (ele.completed) {
        tasksObject[ele.userId] += 1;
      }
    });
  }
  console.log(tasksObject);
});
