#!/usr/bin/env python3
# Educational HTTP header enumeration (authorized lab use only).
import requests, sys
def fetch_headers(url):
    try:
        r = requests.get(url, timeout=8)
        print('Status:', r.status_code)
        for k, v in r.headers.items():
            print(f'{k}: {v}')
    except Exception as e:
        print('Error:', e)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 enum_http_headers.py http://target/')
    else:
        fetch_headers(sys.argv[1])
