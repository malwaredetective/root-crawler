# -----------------------------------------------
# Level: 6
# Difficulty: Easy
# Categories: SUDO, GTFOBins
# Description: The user can escalate privileges due to a GTFOBin.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get install -y \
    gcc

# --- Configure Privilege Escalation Vulnerability ---
# 1. Grants the 'hacker' user passwordless sudo access to /usr/bin/gcc.
COPY d20.c /home/hacker/d20.c
RUN echo "hacker ALL=(ALL) NOPASSWD: /usr/bin/gcc" >> /etc/sudoers && \
echo "Hey I hope your ready for our upcoming session. I'm totally going to make shadowcutie fall for me this time! I'll leave bae'zel to you. :P\n\nI vibe coded a simple dice roller program so that we can stop wasting our time with modifiers. I updated your permissions so you should be able to compile it with: 'sudo gcc -o d20 d20.c'" > /home/hacker/notes.txt && \
chown hacker:hacker /home/hacker/d20.c && \
chown hacker:hacker /home/hacker/notes.txt

# --- Create the Root Flag ---
RUN echo "8ee7c23a901076e22e8b6ec407c190fd" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]