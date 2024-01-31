#!/usr/bin/node
// script that reads and prints the content of a file.
//    -- The first argument is the file path
//    -- The content of the file must be read in utf-8
//    -- If an error occurred during the reading, print the error object

const nfs = require('fs');
const fileName = process.argv[2];

nfs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log("Error occurred:", err);
	  return;
  }
  console.log(data);
})
