#!/usr/bin/node

// Include fs module
const fs = require('fs');

// writes a string to a file.
fs.writeFileSync(process.argv[2], process.argv[3]);
