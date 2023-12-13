#!/usr/bin/node

const list = require('100-data').list;

const list1 = list.map((x, index) => {
  return x * index;
});
console.log(list);
console.log(list1);
