#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status

        - You must use the package requests
        - You are not allow to import packages other than requests
        - The body of the response must be display like the following example
          (tabulation before -)
"""
import requests


if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(resp.text)}")
    print(f"\t- content: {resp.text}")
