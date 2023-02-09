#!/usr/bin/node

const fs = require('fs');

fs(`${process.argv[2]}`, (err, data) => {
  if (err) { console.log(err); } else { console.log(data.toString()); }
});
