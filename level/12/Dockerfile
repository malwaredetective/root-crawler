# -----------------------------------------------
# Level: 12
# Difficulty: Medium
# Categories: Python
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM ubuntu:22.04

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    sudo \
    openssh-server \
    vim \
    nano \
    file \
    cron \
    bsdutils

# --- Create Users ---
RUN useradd -m -s /bin/bash hacker && echo "hacker:hacker" | chpasswd && \
mkdir /var/run/sshd

# --- Download and Configure Linux Privilege Escalation Tools ---
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/

# --- Configure Privilege Escalation Vulnerability ---
RUN echo "\
import random\n\
import os\n\
facts = [\n\
    '1. Disable unused services to reduce your attack surface.',\n\
    '2. Use strong, unique passwords and enable 2FA where possible.',\n\
    '3. Keep your system and all packages up-to-date with security patches.',\n\
    '4. Regularly review user accounts and remove unneeded ones.',\n\
    '5. Use the principle of least privilege: only give users the access they need.'\n\
]\n\
fact = random.choice(facts)\n\
os.system(f'echo \"[Cybersecurity Tip] {fact}\" | wall')\n\
" > /home/hacker/cybersecurityfacts.py && \
chown root:root /home/hacker/cybersecurityfacts.py && \
chmod 644 /home/hacker/cybersecurityfacts.py && \
touch /var/run/utmp /var/log/wtmp && chmod 664 /var/run/utmp /var/log/wtmp && \
echo '* * * * * root PYTHONPATH=/home/hacker python3 /home/hacker/cybersecurityfacts.py' >> /etc/crontab

# --- Create the Root Flag ---
RUN echo "4d9a6b848f0a30e67acaa797e4c68b49" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD bash -c "service cron start; /usr/sbin/sshd -D"
