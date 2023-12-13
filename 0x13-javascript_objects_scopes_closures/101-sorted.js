#!/usr/bin/node

const dict = require('./101-data').dict;

const result = {};

for (const val in dict) {
  const occur = dict[val];

  if (!result[occur]) {
    result[occur] = [];
  }

  result[occur].push(val);
}

console.log(result);
