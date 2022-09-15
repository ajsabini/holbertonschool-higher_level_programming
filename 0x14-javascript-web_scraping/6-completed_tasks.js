#!/usr/bin/node

const urlApi = process.argv[2];
const axios = require('axios');

const obtenerPelicula = async () => {
  try {
    const respuesta = await axios.get(urlApi);
    const diccRetorno = {};
    let val = 0;
    for (let indice = 0; indice < respuesta.data.length; indice++) {
      if (respuesta.data[indice].userId in diccRetorno) {
        if (respuesta.data[indice].completed) {
          val = diccRetorno[respuesta.data[indice].userId].valueOf();

          val++;
          diccRetorno[respuesta.data[indice].userId] = val;
        }
      } else {
        diccRetorno[respuesta.data[indice].userId] = 1;
      }
    }
    console.log(diccRetorno);
  } catch (error) {
    console.log(error);
  }
};
obtenerPelicula();
