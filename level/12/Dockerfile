# -----------------------------------------------
# Level: 12
# Difficulty: Medium
# Categories: Python
# Description: The can hijack a python script via a misconfigured cron job.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get install -y \
    bsdutils

# --- Configure Privilege Escalation Vulnerability ---
# 1. Writes a Python script to /home/hacker/cybersecurityfacts.py that, when run, prints a random security tip to all users using wall.
# 2. Sets the script's ownership to root but permissions to 644 (world-readable and world-writable). 
# 3. Sets up a cron job (in /etc/crontab) to run the script every minute as root.
# 4. Prepares utmp and wtmp files with permissions so wall will not fail.
COPY cybersecurityfacts.py /home/hacker/cybersecurityfacts.py

RUN chown root:root /home/hacker/cybersecurityfacts.py && \
chmod 644 /home/hacker/cybersecurityfacts.py && \
touch /var/run/utmp /var/log/wtmp && chmod 664 /var/run/utmp /var/log/wtmp && \
echo '* * * * * root PYTHONPATH=/home/hacker python3 /home/hacker/cybersecurityfacts.py' >> /etc/crontab

# --- Create the Root Flag ---
RUN echo "4d9a6b848f0a30e67acaa797e4c68b49" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD bash -c "service cron start; /usr/sbin/sshd -D"
