#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    site = sys.argv[1]
    url = urllib.request.Request(site)

    with urllib.request.urlopen(url) as e:
        header_dict = e.headers
        print(header_dict['X-Request-Id'])
