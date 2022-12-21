#!/usr/bin/node

const fs = require('fs');

const data1 = fs.readFileSync(`./${process.argv[0]}`, { encoding: 'utf-8', flag: 'r' });
const data2 = fs.readFileSync(`./${process.argv[1]}`, { encoding: 'utf-8', flag: 'r' });

const data3 = data1 + data2;

fs.writeFileSync(`./${process.argv[2]}`, data3, 'utf-8');
