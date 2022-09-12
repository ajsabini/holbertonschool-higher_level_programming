#!/usr/bin/node

const file = process.argv[2];
const axios = require('axios');

axios
  .get(file)
  .then(res => {
    console.log(`code: ${res.status}`);
    // console.log(res);
  })
  .catch(error => {
    console.log(`code: ${error.response.status}`);
  });
