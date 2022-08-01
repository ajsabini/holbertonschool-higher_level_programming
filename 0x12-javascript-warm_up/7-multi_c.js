#!/usr/bin/node

const cant = parseInt(process.argv[2], 10);
if (isNaN(cant)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = cant; i > 0; i--) {
    console.log('C is fun');
  }
}
