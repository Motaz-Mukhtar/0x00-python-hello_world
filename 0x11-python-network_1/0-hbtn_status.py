#!/usr/bin/python3
"""
    Script that Fetches https://alx-intarnet.hbtn.io/status
"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        b = response.read()
        print("Body reponse:")
        print("\t- type: {}".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf8 content: {}".format(b.decode('utf-8')))
