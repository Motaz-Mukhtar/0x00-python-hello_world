#!/usr/bin/node

function recurs (n) {
  if (n >= 1) {
    return n * recurs(n - 1);
  } else { return 1; }
}
console.log(recurs(+process.argv[2]));
