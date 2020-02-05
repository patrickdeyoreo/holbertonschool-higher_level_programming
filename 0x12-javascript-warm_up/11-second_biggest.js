#!/usr/bin/node
// Searches for the second biggest integer in a list of arguments
const numbers = process.argv.slice(2).map(x => parseInt(x));
if (numbers.length < 2) {
  console.log(0);
} else {
  console.log([...new Set(numbers)].sort((a, b) => b - a)[1]);
}
