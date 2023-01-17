#!/usr/bin/python3
""" Dispaly sthe value of the X-Request-Id varibale found in the header """
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(req) as response:
        print(response.headers["X-Request-Id"])
        print(response.headers)
