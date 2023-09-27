#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieURL, (error, response, body) => {
  if (error) return console.error(error);
  const movie = JSON.parse(body);

  movie.characters.forEach((character) => {
    request.get(character, (error, response, body) => {
      if (error) return console.error(error);
      const person = JSON.parse(body);
      console.log(person.name);
    });
  });
});
