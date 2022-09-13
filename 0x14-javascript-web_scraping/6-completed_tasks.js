#!/usr/bin/node

const urlApi = process.argv[2];
const axios = require('axios');
let cuantos = 0;
let cambioUserId = 0;

const obtenerPelicula = async () => {
  try {
    const respuesta = await axios.get(urlApi);
    const diccRetorno = {};

    // console.log(respuesta.data.length);

    for (let indice = 0; indice < respuesta.data.length; indice++) {
      if (respuesta.data[indice].userId !== cambioUserId) {
        if (cambioUserId !== 0) {
        // console.log(cambioUserId + ' ' + cuantos);
          diccRetorno[cambioUserId] = cuantos;
        }
        cambioUserId = respuesta.data[indice].userId;
        cuantos = 0;
      }
      if (respuesta.data[indice].completed) {
        cuantos++;
      }
      /*
      if (indice === respuesta.data.length - 1) {
        if (respuesta.data[respuesta.data.length - 2].userId === respuesta.data[respuesta.data.length - 1].userId) {
        // console.log(cambioUserId + ' ' + cuantos);
          diccRetorno[cambioUserId] = cuantos;
        }
      } */
    }
    diccRetorno[cambioUserId] = cuantos;
    console.log(diccRetorno);
  } catch (error) {
    console.log(error);
  }
};
obtenerPelicula();
