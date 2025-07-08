#!/usr/bin/node
function countArgs () {
  return arguments.length;
}

if (countArgs() === 0) {
  console.log('No argument');
} else if (countArgs() === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
