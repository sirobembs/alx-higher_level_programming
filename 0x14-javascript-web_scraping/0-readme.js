#!/usr/bin/node

// Include fs module
const fs = require('fs');

// Use fs.readFile() method to read the file
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (data === undefined) {
    console.log(err);
  } else {
    console.log(data);
  }
});
