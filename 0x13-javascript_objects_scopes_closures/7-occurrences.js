#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  const len = list.length;

  for (let i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      num++;
    }
  }
  return num;
};
