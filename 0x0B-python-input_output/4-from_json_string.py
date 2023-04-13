#!/usr/bin/python3
"""This module defines a JSON decoding function."""
import json


def from_json_string(my_str):
    """function that returns an object"""
    return json.loads(my_str)
