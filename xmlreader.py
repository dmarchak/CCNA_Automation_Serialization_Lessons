#! /usr/bin/env python3

"""Demonstrate using xmltodict to read XML data."""

import os
import xmltodict

# Use file path relative to the script's location
base = os.path.dirname(__file__)
xml_path = os.path.join(base, 'r1.xml')

# Read the XML file
with open(xml_path, encoding='utf-8') as file:
    xml_data = file.read()

# Convert XML data to a Python dictionary
dict_data = xmltodict.parse(xml_data)

# Accessing nested data in the dictionary
print(dict_data['router']['interfaces']['interface'][0]['ip'])
