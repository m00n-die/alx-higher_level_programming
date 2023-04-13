#!/usr/bin/python3
"""This module defines a JSON decoding function."""
import json


def to_json_string(my_obj):
    """function that returns an object"""
    return json.loads(my_obj)