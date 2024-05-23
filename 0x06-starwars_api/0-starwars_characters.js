#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }

  const characters = JSON.parse(body).characters;
  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('error:', error);
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
