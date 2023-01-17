#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the
    URL and displays the body of the response
"""
import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            code_status = response.code
            print(response.read())
    except HTTPError as e:
        print(f"Error code: {e.code}")
