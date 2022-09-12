#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const axios = require('axios');
const fs = require('fs');

const obtenerContenido = async () => {
  const respuesta = await axios.get(url);
  fs.writeFile(file, respuesta.data, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
};

obtenerContenido();
/*
fs.writeFile(file, stringWrite, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
}); */
