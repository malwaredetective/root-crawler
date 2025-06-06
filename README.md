# Root Crawler 🐧

A hands-on, gamified experience for learning Linux Privilege Escalation, powered by Docker!

## 🧩 What is Root Crawler?

Root Crawler turns learning Linux privilege escalation into an exciting game! With each 'level,' you'll face a unique challenge, safely contained within a Docker environment. Solve real-world scenarios, uncover hints to guide you, and track your progress as you grow your skills and confidence. Whether you're an aspiring ethical hacker or a seasoned pro looking to refine your techniques, Root Crawler offers a gamified, hands-on learning experience that's as rewarding as it is fun.

- 🔥 **Randomized Encounters**: Roll the dice and spin up a random instance. Can you escalate your privileges to root and capture the flag?
- 🤖 **Hints and Progress Tracking**: Your journey, your rules. Ask for hints when your stuck, and track your victories along the way.
- 🐳 **Easy Clean-Up**: Done pwning? Sweep away all project containers and images with ease.

## 📋 Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)

## ⚡ Quickstart Guide

### 1. Clone the Repository

```bash
git clone https://github.com/malwaredetective/root-crawler.git
cd root-crawler
```

### 2. Set Up a Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate    # (Windows: venv\Scripts\activate)
```
### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify that Docker is Running
```bash
docker info
```

> If you get an error, make sure Docker Desktop or your Docker service is running.

### 5. Launch a Random Instance and start Hacking!
```bash
python3 ./root-crawler.py --random
```

```
(venv) khub@khub-desktop:/mnt/c/Users/Khub/source/repos/root-crawler/root-crawler-main$ python3 ./root-crawler.py --random
 ____             _      ____                    _
|  _ \ ___   ___ | |_   / ___|_ __ __ ___      _| | ___ _ __
| |_) / _ \ / _ \| __| | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
|  _ < (_) | (_) | |_  | |___| | | (_| |\ V  V /| |  __/ |
|_| \_\___/ \___/ \__|  \____|_|  \__,_| \_/\_/ |_|\___|_|


[INFO] Choosing a random level ...
[INFO] Level 4
[INFO] Difficulty: hard
[INFO] Credentials: `hacker:hacker`
[INFO] Creating your instance ...
[SUCCESS] Docker build completed successfully!
[SUCCESS] Your instance was successfully deployed!
[INFO] Log into your instance with SSH: `ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no hacker@127.0.0.1 -p 2222`
[CHALLENGE] Can you escalate your privileges to root and get the flag!?
```

## 🚀 Usage

`python3 root-crawler.py --help`

| Command | Description |
| --- | --- |
| --random | Play a random, uncompleted level |
| --level # | Play a specific level (e.g. --level 2) |
| --hint | Show a hint for your current level |
| --flag FLAG | Submit a flag (e.g. --flag 12345) |
| --progress | See your completion progress |
| --reset | Reset all progress in the local database |
| --status | Show details about the current active level |
| --stop |	Stop all active root-crawler containers |
| --purge |	Stop & remove all containers and images for this project |

# 🛡️ Clean Up
To free disk space and clear all project resources:

`python3 root-crawler.py --purge`
This removes all project containers and images. You can restart from scratch any time!

## 📝 License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this project in accordance with the license terms.
