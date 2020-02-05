#!/usr/bin/node
// Define a function increment a value and apply a function to it
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
