#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]));
