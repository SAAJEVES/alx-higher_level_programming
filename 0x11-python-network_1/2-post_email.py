#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    site = sys.argv[1]
    email = sys.argv[2]

    data = {}
    data["email"] = email

    data_email = urllib.parse.urlencode(data)
    data_email = data_email.encode('ascii')

    req = urllib.request.Request(site, data_email)

    with urllib.request.urlopen(req) as resp:
        resp_value = response.read()
        print(f"Your email is: {resp_value.decode('utf-8')}")
