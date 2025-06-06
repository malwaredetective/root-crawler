#!/usr/bin/python3
import subprocess
import base64
import re

out = subprocess.check_output(["/usr/local/bin/exiftool", "/home/hacker/secret-message.png"]).decode()
match = re.search(r'Comment\s+:\s*([A-Za-z0-9+/=]+)', out)
if match:
    b64 = match.group(1)
    try:
        decoded = base64.b64decode(b64).decode()
        print(decoded)
    except Exception as e:
        print("Failed to decode base64:", e)
else:
    print("No base64 comment found!")
