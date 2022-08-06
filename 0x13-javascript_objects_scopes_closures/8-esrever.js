#!/usr/bin/node

exports.esrever = function (list) {
  const revert = [];
  const largo = list.length;
  for (let i = largo - 1; i >= 0; i--) {
    revert.push(list[i]);
  }
  return (revert);
};
