#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  a = parseInt(argv[2]);
  b = parseInt(argv[3]);
  console.log(a + b);
}
