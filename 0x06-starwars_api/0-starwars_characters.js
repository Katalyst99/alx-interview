#!/usr/bin/node
const request = require('request');
const id = process.argv;

request(`https://swapi-api.alx-tools.com/api/films/${id[2]}`, function (e, response, body) {
  if (e) {
    console.error('Error:', e);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Failed to fetch starwars data. Status code: ${response.statusCode}`);
  }

  try {
    const starwars = JSON.parse(body);
    const characters = starwars.characters;
    const fetchCharacter = (url) => {
      return new Promise((resolve, reject) => {
        request(url, function (chErr, chResp, chBody) {
          if (chErr || !chResp || chResp.statusCode !== 200) {
            reject(chErr);
          } else {
            const chName = JSON.parse(chBody).name;
            resolve(chName);
          }
        });
      });
    };

    (async () => {
      for (const cha of characters) {
        try {
          const name = await fetchCharacter(cha);
          console.log(name);
        } catch (err) {
          console.error('Error fetching character:', err);
        }
      }
    })();
  } catch (parseE) {
    console.error('Error parsing response:', parseE);
  }
});
