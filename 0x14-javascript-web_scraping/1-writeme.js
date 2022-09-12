#!/usr/bin/node

const file = process.argv[2];
const stringWrite = process.argv[3];
const fs = require('fs');

fs.writeFile(file, stringWrite, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
