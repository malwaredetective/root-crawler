# -----------------------------------------------
# Level: 18
# Difficulty: 
# Categories: CVE
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    build-essential \
    openssh-server \
    vim \
    nano \
    file \
    cron \
    gcc \
    make \
    net-tools \
    netcat \
    libpam0g-dev \
    libutempter0 \
    libutempter-dev \
    libncurses5-dev \
    libncursesw5-dev

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
WORKDIR /tmp
COPY screen-4.5.0.tar.gz /tmp/screen-4.5.0.tar.gz

RUN tar xzf screen-4.5.0.tar.gz && \
cd screen-4.5.0 && \
./configure && \
make && \
make install && \
rm -rf /tmp/*

RUN echo '#!/bin/bash\nwhile true; do uptime >> /tmp/activity.log; sleep 20; done' > /usr/local/bin/background.sh && \
    chmod +x /usr/local/bin/background.sh

# --- Create the Root Flag ---
RUN echo "66ffe0e495cd6d7a3f550c3c72989616" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD service ssh start && \
    screen -dmS sysmon /usr/local/bin/background.sh && \
    tail -f /dev/null

