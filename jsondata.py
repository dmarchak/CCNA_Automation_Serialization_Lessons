#! /usr/bin/env python3

"""Demonstrate using json to read and write JSON data."""

import os
import json

# json.load() - Read JSON data from a file and convert it to a Python dictionary
# json.dump() - Write a Python dictionary to a file in JSON format

# json.loads() - Convert a JSON string to a Python dictionary
# json.dumps() - Convert a Python dictionary to a JSON string

# Use file path relative to the script's location
base = os.path.dirname(__file__)
json_path = os.path.join(base, 'r1.json')

# Read the JSON file
# with open(json_path, encoding='utf-8') as file:
#     # Convert JSON data to a Python dictionary using JSON load
#     json_data = json.load(file)

ROUTER_DICT = {
    "router": {
        "hostname": "R1",
        "interfaces": [
            {
                "id": "0",
                "enabled": "true",
                "name": "GigabitEthernet0/0",
                "ip": "192.168.1.254",
                "mask": "255.255.255.0"
            },
            {
                "id": "1",
                "enabled": "true",
                "name": "GigabitEthernet0/1",
                "ip": "172.16.1.2",
                "mask": "255.255.255.0"
            }
        ],
        "routing": {
            "routes": [
                {
                    "destination": "192.168.2.0",
                    "mask": "255.255.255.0",
                    "gateway": "192.168.1.253"
                },
                {
                    "destination": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "gateway": "201.1.113.54"
                }
            ]
        }
    }
}

# ROUTER_JSON = json.dumps(ROUTER_DICT)
# print(ROUTER_JSON)

with open(os.path.join(base, 'data.json'), 'w', encoding='utf-8') as file:
    json.dump(ROUTER_DICT, file, indent=4)

# json_data = json.loads(ROUTER_JSON)

# Accessing nested data in the dictionary
# print(json_data['router']['interfaces'][0]['ip'])
