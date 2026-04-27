#! /usr/bin/env python3

"""Demonstrate using pyyaml to read and write YAML data."""

# imports
import os
import yaml

# Set relative file path to the YAML file
yaml_path = os.path.join(os.path.dirname(__file__), 'r1.yml')

# yaml.safe_load() - Read YAML data from a file and convert it to a Python dictionary
# yaml.safe_dump() - Write a Python dictionary to a file in YAML format
with open(yaml_path, encoding='utf-8') as file:
    yaml_data = yaml.safe_load(file)

# display the data read from the YAML file
print(yaml_data)
