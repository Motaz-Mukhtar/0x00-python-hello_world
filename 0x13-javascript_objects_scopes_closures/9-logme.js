#!/usr/bin/node

const list = [];

exports.logMe = function (item) {
  list.push(item);
  console.log(`${list.length - 1}: ${list[list.length - 1]}`);
};
