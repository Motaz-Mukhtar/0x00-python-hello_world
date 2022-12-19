#!/usr/bin/node

const arr = process.argv.sort();

if (arr.length <= 3) console.log(0);
else console.log(arr[arr.length - 2]);
