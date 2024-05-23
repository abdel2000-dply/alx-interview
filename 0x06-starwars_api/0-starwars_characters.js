#!/usr/bin/node
const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map((characterUrl) => requestPromise(characterUrl));
    const characterResponses = await Promise.all(characterPromises);
    characterResponses.forEach((characterResponse) => {
      console.log(JSON.parse(characterResponse.body).name);
    });
  }
});