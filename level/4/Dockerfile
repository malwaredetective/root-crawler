# -----------------------------------------------
# Level: 4
# Difficulty: Easy
# Categories: Weak File Permissions
# Description: /etc/passwd is writeable.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest

# --- Create Users ---
RUN useradd -m -s /bin/bash george && echo "george:Winter25" | chpasswd 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Set write permissions on /etc/passwd.
RUN groupadd editors && usermod -a -G editors george && chgrp editors /etc/passwd && chmod 664 /etc/passwd  && \
mkdir -p /home/george/.scripts && \ 
echo "* * * * * george /bin/bash /home/george/.scripts/backdoor.sh &" >> /etc/crontab && \
echo "I've managed to setup a little bird on another users account.\n\nIt's a bind shell running on port 1337. It's setup on a timer to trigger once a minute.\n\nFinish the job and get us root access on this box!\n\nGood luck,\n\nMaster of Whisperers" > /home/hacker/letter.txt && \
chown hacker:hacker /home/hacker/letter.txt && chmod 600 /home/hacker/letter.txt

COPY backdoor.sh /home/george/.scripts/backdoor.sh

RUN chown -R george:george /home/george/.scripts \
 && chmod 700 /home/george/.scripts \
 && chmod 700 /home/george/.scripts/backdoor.sh

RUN echo "# The Winds of Winter\n\n**TO DO**: Write a book ...\n\nBy GRRM" > /home/george/the-winds-of-winter.md && \
chown george:george /home/george/the-winds-of-winter.md && chmod 600 /home/george/the-winds-of-winter.md

# --- Create the Root Flag ---
RUN echo "b93841e55f11579f2203690ce64be128" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD service cron start && /usr/sbin/sshd -D
