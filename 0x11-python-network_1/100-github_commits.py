#!/usr/bin/python3
# d
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    req = requests.get("https://api.github.com/repos/{}/{}/commits".
                       format(sys.argv[1], sys.argv[2]))

    num = 1
    data = req.json()
    print(type(data))
    for lists in data:
        print("{}: {}".format(lists.get("sha"), lists.get("commit").get("author").get("name")))
        if num == 10:
            break
        num += 1
