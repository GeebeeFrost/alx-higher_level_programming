#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) return console.error(error);
  const todos = JSON.parse(body);

  const completed = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (!completed[todo.userId]) completed[todo.userId] = 1;
      else completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
