#!/usr/bin/python3
import sys
import requests

req = requests.get("http://alxweb-01.tech")
print(req.text)
