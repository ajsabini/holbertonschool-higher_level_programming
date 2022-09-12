#!/usr/bin/node

let file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', function(err, ret) {
	if (err) {
		console.log(err);
	} else {
		console.log(ret);
	}
});
