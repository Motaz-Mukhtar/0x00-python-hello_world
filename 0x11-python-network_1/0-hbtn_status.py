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
        print("     - type: {}".format(type(b)))
        print("     - content: {}".format(b))
        print("     - utf8 content: {}".format(b.decode('utf-8')))
