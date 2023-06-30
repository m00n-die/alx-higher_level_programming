#!/bin/bash
# sends a post request to a url
curl -s -X POST -d "email: test@gmail.com&subject: I will always be here for PLD" "$1"
