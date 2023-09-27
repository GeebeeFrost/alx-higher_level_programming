#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) return console.error(error);
  fs.writeFile(filename, body, (error) => {
    if (error) return console.error(error);
  });
});
