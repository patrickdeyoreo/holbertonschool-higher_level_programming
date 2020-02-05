#!/usr/bin/node
// Define a function to add two integers
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i += 1) {
    theFunction();
  }
};
