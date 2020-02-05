#!/usr/bin/node
// Define a function to add two integers
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
