# 0x06-starwars_api

This is a repository for the 0x06-starwars_api project.

## Description

This project involves creating a Node.js script that interacts with the [Star Wars API](https://swapi-api.alx-tools.com/) to fetch and display information about Star Wars characters based on a movie ID provided as a command-line argument.

The script uses the `request` module to make HTTP requests and handles asynchronous operations using callbacks. It parses JSON data returned by the API and displays one character name per line in the same order as the "characters" list in the `/films/` endpoint.

## Usage

To run the script, use the following command:

```bash
./0-starwars_characters.js <movie_id>