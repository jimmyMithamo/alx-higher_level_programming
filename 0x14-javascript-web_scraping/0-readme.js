#!/usr/bin/node
// a script that reads content from a file

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
