#!/bin/bash
# sends a post request to a url

curl -s -X POST "$1" -d "email: test@gmail.com&subject: I will always be here for PLD"
