#!/usr/bin/node

const mylist = require('./100-data.js').list;
console.log(mylist);

const newlist = mylist.map((x, index) => x * index);

console.log(newlist);
