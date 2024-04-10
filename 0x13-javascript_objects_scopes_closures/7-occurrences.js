#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let add = 0;
  const se = searchElement;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === se) {
      add += 1;
    }
  }
  return add;
};
