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

nrequest(url, (error, response) => {
  if (error) {
    console.log(error.message);
    return;
  }
  console.log('code:', response.statusCode);
});
