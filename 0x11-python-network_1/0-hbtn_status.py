#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as resp:
        body = resp.read()
        content = body.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {content}")
