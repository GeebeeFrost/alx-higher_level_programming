#!/usr/bin/node

const arg = Number.parseInt(process.argv[2]);

if (!Number.isInteger(arg)) console.log('Missing size');
else {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}