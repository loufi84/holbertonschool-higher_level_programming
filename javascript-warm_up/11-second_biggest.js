#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 4) {
  console.log('0');
} else {
  const numbers = argv.slice(2);
  const intNum = numbers.map(n => parseInt(n));
  intNum.sort((a, b) => b - a);
  console.log(intNum[1]);
}
