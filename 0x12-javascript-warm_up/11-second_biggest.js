#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const numeros = process.argv.slice(2);
  numeros.sort(function (a, b) {return b - a;});
  console.log(numeros[1]);
}
