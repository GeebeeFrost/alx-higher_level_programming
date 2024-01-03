#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (err, res, body) => {
  if (err) return console.error(err);
  const films = JSON.parse(body);
  films.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes('18')) count += 1;
    });
  });
  console.log(count);
});
