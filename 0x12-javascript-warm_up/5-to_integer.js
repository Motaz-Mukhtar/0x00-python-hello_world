#!/usr/bin/node
const num = +process.argv[2];
if (!isNaN(num)) {
  console.log(`My number: ${+process.argv[2]}`);
} else console.log('Not a number');
