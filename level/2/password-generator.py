#!/usr/bin/python3
import random

nouns = [
    "dragon", "matrix", "raven", "server", "kernel", "botnet", "shell", "rootkit", "daemon", "packet"
]
hacker_words = [
    "pwn", "phreak", "zero", "crypto", "exploit", "ninja", "ghost", "shadow", "worm", "overflow"
]

def main():
    noun = random.choice(nouns)
    hacker = random.choice(hacker_words)
    num = random.randint(0, 9)
    password = f"{noun.capitalize()}{hacker}{num}"
    print(password)

if __name__ == "__main__":
    main()
