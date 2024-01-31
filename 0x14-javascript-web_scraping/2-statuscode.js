#!/usr/bin/node

/*
script that display the status code of a GET request.
  -- The first argument is the URL to request (GET)
  -- The status code must be printed like this: code: <status code>
  -- You must use the module request
*/
const nrequest = require('request');
const cliArg = process.argv;
const url = cliArg[2];

nrequest(url, (err, response, body) => {
  if (err) {
    console.log('Error occurred:', err.message);
    return;
  }
  console.log('Code', response.statusCode);
});
