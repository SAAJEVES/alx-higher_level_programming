#!/usr/bin/node

/*
Write a script that gets the contents of a webpage and stores it in a file.

  -- The first argument is the URL to request
  -- The second argument the file path to store the body response
  -- The file must be UTF-8 encoded
  -- You must use the module request
*/

const nreq = require('request');
const fs = require('fs');

nreq(process.argv[2], function (_err, _res, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
