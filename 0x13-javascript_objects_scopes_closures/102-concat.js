#!/usr/bin/node

const fs = require('fs');

const data1 = fs.readFileSync(`./${process.argv[2]}`, 'utf-8');
const data2 = fs.readFileSync(`./${process.argv[3]}`, 'utf-8');

const data3 = data1 + data2;

fs.writeFileSync(`./${process.argv[4]}`, data3);
