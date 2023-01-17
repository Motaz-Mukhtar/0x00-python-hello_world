#!/usr/bin/python3
"""
    Script that takes in a URL and an email
    Sends a POST request to the passed URL
    with the email as a parameter, and
    finally displays the body of the
    reponse.
"""
import sys
import requests


if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(req.text)
