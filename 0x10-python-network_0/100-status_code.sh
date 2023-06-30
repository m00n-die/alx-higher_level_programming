#!/bin/bash
# gets status code
curl -s -o /dev/null -w "%{http_code}" "$1"
