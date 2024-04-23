#!/usr/bin/node
// a script that writes into  a file

const fs = require('fs');
const path = process.argv[2];
const messageString = process.argv[3];

fs.writeFile(path, messageString, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
