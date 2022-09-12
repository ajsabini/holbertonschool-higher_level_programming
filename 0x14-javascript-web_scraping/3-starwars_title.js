#!/usr/bin/node

const idMovie = process.argv[2];
const axios = require('axios');

const obtenerPelicula = async () => {
  const respuesta = await axios.get('https://swapi-api.hbtn.io/api/films/' + idMovie);
  console.log(respuesta.data.title);
};
obtenerPelicula();
