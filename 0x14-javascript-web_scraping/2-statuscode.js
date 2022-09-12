#!/usr/bin/node

let file = process.argv[2];
const axios = require('axios');

axios
	.get(file)
	.then(res => {
		console.log(`statusCode: ${res.status}`);
		console.log(res);
	})
	.catch(error => {
		console.error(error);
	});
