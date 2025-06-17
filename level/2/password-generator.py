#!/usr/bin/python3
import random

nouns = [
    "botnet", "dragon", "raven", "shell", "rootkit"
]
hacker_words = [
    "pwn", "exploit", "ghost", "worm", "overflow"
]

def main():
    noun = random.choice(nouns)
    hacker = random.choice(hacker_words)
    num = random.randint(0, 9)
    password = f"{noun.capitalize()}{hacker}{num}"
    print(password)

if __name__ == "__main__":
    main()
