#!/bin/bash
set -e

git config --global user.email "hacker@root-crawler-level-19"
git config --global user.name "hacker"
mkdir -p /opt/simple-vuln-scanner
cd /opt/simple-vuln-scanner
git init

# README
echo "# simple-vuln-scanner\n" > README.md
echo "Welcome to simple-vuln-scanner, a basic vulnerability scanner for pentesters.\n" >> README.md
echo "This app queries a local database for credentials and then performs a light-weight directory scan against a local web app that's secured with basic authentication.\n" >> README.md

# Config
echo "scan_interval: 3600" > config.yaml

# main.py
cat > main.py <<EOF
#!/usr/bin/env python3
import sqlite3
import base64
import requests

def get_admin_password():
    try:
        conn = sqlite3.connect('/opt/simple-vuln-scanner/credentials.db')
        c = conn.cursor()
        c.execute('SELECT password FROM users WHERE username="admin"')
        pw = c.fetchone()
        conn.close()
        if pw:
            return pw[0]
        else:
            print("Admin user not found in DB.")
            return None
    except Exception as e:
        print(f"Error querying database: {e}")
        return None

def basic_auth_header(user, pw):
    import base64
    credential = f"{user}:{pw}"
    encoded = base64.b64encode(credential.encode()).decode()
    return {'Authorization': f'Basic {encoded}'}

def dir_scan(base_url, paths, auth_header):
    for path in paths:
        url = f"{base_url}/{path}"
        try:
            response = requests.get(url, headers=auth_header, timeout=5)
            print(f"[{response.status_code}] {url}")
        except requests.RequestException as e:
            print(f"Could not connect to {url}: {e}")

def main():
    print("Starting simple-vuln-scanner...")
    admin_pw = get_admin_password()
    if not admin_pw:
        print("No admin password, aborting scan.")
        return
    print(f"[*] Retrieved admin password from DB.")
    base_url = "http://root-crawler-level-19.local"
    paths = ["admin", "login", "dashboard", ".git", "robots.txt"]
    headers = basic_auth_header("admin", admin_pw)
    dir_scan(base_url, paths, headers)

if __name__ == "__main__":
    main()
EOF

chmod +x main.py

git add .
git commit -m "Initial commit: project files"

# Create SQLite DB with admin creds
sqlite3 credentials.db "CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT);"
sqlite3 credentials.db "INSERT INTO users VALUES ('admin', '${ROOTPW}');"

git add credentials.db
git commit -m "Added SQLite DB with administrative credentials"

# Now reset the admin password in the DB for "security concerns"
sqlite3 credentials.db "UPDATE users SET password='letitSNOWletitSNOW25' WHERE username='admin';"
git add credentials.db
git commit -m "Reset the password for security concerns. Password re-use is a common mistake and I have to be better at always using the same password for everything."

