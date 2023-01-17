#!/usr/bin/python3
""" Python script that takes in a URL and
    an email, sends a POST request to the
    passed URL with the email as a parameter,
    and displays the body of the reponse
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    request = urllib.parse.urlencode(sys.argv[2])
    request = request.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], request) as reponse:
        print(reponse.read().decode('utf-8'))
        print(reponse.code)
