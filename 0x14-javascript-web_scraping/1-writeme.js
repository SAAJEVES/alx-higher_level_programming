#!/usr/bin/node

/*
a script that writes a string to a file.
  -- The first argument is the file path
  -- The second argument is the string to write
  -- The content of the file must be written in utf-8
  -- If an error occurred during while writing, print the error object
 **/

const nfs = require('fs');

const cliArg = process.argv;
const fileName = cliArg[2];
const fileContent = cliArg[3];

nfs.writeFile(fileName, fileContent, 'utf-8', (err) => {
  if (err) {
    console.log('Error occurred:', err);
  }
});
