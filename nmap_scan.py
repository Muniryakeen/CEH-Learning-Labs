#!/usr/bin/env python3
# Educational nmap wrapper for authorized lab use only.
import subprocess, sys
def basic_scan(target):
    print(f"Would run nmap against {target} (lab only).")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 nmap_scan.py <target>")
    else:
        basic_scan(sys.argv[1])
