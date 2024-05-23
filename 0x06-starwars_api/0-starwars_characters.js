#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }

  const characters = JSON.parse(body).characters;
  const characterPromises = characters.map(fetchCharacterName);

  Promise.all(characterPromises)
    .then(names => names.forEach(name => console.log(name)))
    .catch(error => console.error('error:', error));
});
