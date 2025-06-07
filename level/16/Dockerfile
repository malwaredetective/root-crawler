# -----------------------------------------------
# Level: 16
# Difficulty: Medium
# Categories: Cron Jobs
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Configure Privilege Escalation Vulnerability ---
# 1. /usr/local/bin/backup.py is created as a world-readable, world-writable shell script (755).
# 2. A root cron job runs this script every minute.
# 3. Any user (including 'hacker') can overwrite this script, so arbitrary code is executed as root—this is the privilege escalation vector.
RUN echo '#!/bin/sh\ncd /home/hacker\ntar czf /tmp/backup.tar.gz *' > /usr/local/bin/backup.py && chmod 755 /usr/local/bin/backup.py && \
echo '* * * * * root /usr/local/bin/backup.py' >> /etc/crontab

# --- Create the Root Flag ---
RUN echo "eaed4b44cef9917de41953cc2f2a0806" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD bash -c "service cron start; /usr/sbin/sshd -D"
