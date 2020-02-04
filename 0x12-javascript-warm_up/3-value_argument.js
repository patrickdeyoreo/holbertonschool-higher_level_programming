#!/usr/bin/node
// Print the first argument if any are provided
if (process.argv.length > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
