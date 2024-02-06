#!/usr/bin/node
/*
script that prints all characters of a Star Wars movie:

  -- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
  -- Display one character name by line
  -- You must use the Star wars API
  -- You must use the module request
*/
const nreq = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

nreq(api, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
