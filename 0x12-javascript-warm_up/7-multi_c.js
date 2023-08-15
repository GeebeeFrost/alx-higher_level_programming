#!/usr/bin/node

const arg = Number.parseInt(process.argv[2]);

if (!Number.isInteger(arg)) console.log('Missing number of occurences');
else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
