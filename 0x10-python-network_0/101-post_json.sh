#!/bin/bash
# post JSOn data
curl -s -X POST "$1" -d @"$2"
