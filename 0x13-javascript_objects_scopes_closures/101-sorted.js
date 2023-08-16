#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const [k, v] of Object.entries(dict)) {
  (newDict[v]) ? newDict[v].push(k) : newDict[v] = [k];
}
console.log(newDict);
