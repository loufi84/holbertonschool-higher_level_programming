#!/usr/bin/node
const { argv } = require('node:process');

argv.forEach((val, index) => {
  if (index === 0) {
    console.log('No argument');
  } else if (index === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
});
