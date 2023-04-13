#!/usr/bin/python3
"""This module defines a JSON encoding function."""
import json


def to_json_string(my_obj):
    """function that returns json string"""
    return json.dumps(my_obj)