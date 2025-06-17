# -----------------------------------------------
# Level: 16
# Difficulty: Hard
# Categories: Cron Jobs
# Description: A misconfigured cron job can be exploited via wild card expansion.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get install -y \
    python3-pip \
    python3-flask


# --- Configure Privilege Escalation Vulnerability ---
# 1. /usr/local/bin/backup.py is created as a world-readable, world-writable shell script (755).
# 2. A root cron job runs this script every minute.
RUN echo "URL: http://127.0.0.1:5000/demo \nUsername: hacker\nPassword: iwantACC3\$\$totheDEMO!\n\nMake sure you don't lose these credentials!" > /home/hacker/credentials.txt && \
echo '#!/bin/sh\ncd /home/hacker\ntar czf /tmp/backup.tar.gz *' > /usr/local/bin/backup.py && chmod 755 /usr/local/bin/backup.py && \
echo '* * * * * root /usr/local/bin/backup.py' >> /etc/crontab && \
mkdir /root/demo

COPY app.py /root/demo/app.py
COPY templates /root/demo/templates

# --- Create the Root Flag ---
RUN echo "eaed4b44cef9917de41953cc2f2a0806" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD bash -c "service cron start; python3 /root/demo/app.py & /usr/sbin/sshd -D"
