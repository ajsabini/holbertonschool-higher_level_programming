#!/usr/bin/node

const urlApi = process.argv[2];
const axios = require('axios');
let cuantos = 0;
// console.log(urlApi);
const obtenerPelicula = async () => {
  const respuesta = await axios.get(urlApi);
  // console.log(respuesta.data.results[0].characters);
  // console.log(respuesta.data.results.length);
  for (let indice = 0; indice < respuesta.data.results.length; indice++) {
    // console.log(respuesta.data.results[indice].characters.length);
    for (let indChars = 0; indChars < respuesta.data.results[indice].characters.length; indChars++) {
      // console.log(respuesta.data.results[indice].characters[indChars]);
      if (respuesta.data.results[indice].characters[indChars].includes('18')) {
        cuantos++;
      }
    }
  }
  console.log(cuantos);
};
obtenerPelicula();

/*
 console.log(respuesta.data.results[0].characters);
 accedo a loscharater de la peliculamen la pos 0
*/
