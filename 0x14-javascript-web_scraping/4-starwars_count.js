#!/usr/bin/node

/*
script that prints the number of movies where the character “Wedge Antilles” is present.
  -- The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
  -- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
  -- You must use the module request
*/
const nreq = require('request');
const cliArg = process.argv;
const api = cliArg[2];

nreq(api, (err, resp, body) => {
  if (err) {
    console.log(err.message);
    return;
  }
  let times;
  const body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }
});
