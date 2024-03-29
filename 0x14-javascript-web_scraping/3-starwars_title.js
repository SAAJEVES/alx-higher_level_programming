#!/usr/bin/node
/*
script that prints the title of a Star Wars movie where the episode number matches a given integer.
  -- The first argument is the movie ID
  -- You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
  -- You must use the module request
*/
const nreq = require('request');
const cliArg = process.argv;
const id = cliArg[2];
const api = `https://swapi-api.alx-tools.com/api/films/${id}`;

nreq(api, (err, resp, body) => {
  if (err) {
    console.log(err.message);
    return;
  }
  const result = JSON.parse(body);
  console.log(result.title);
});
