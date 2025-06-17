# -----------------------------------------------
# Name: root-crawler
# Description: A base Ubuntu image for challenges hosted at: https://github.com/malwaredetective/root-crawler.git.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM ubuntu:24.04

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    sudo \
    openssh-server \
    vim \
    nano \
    file \
    cron \
    net-tools \
    netcat-openbsd \ 
    tmux \ 
    libcap2-bin \
    git \
    curl \
    dos2unix

# --- Create Users ---
RUN useradd -m -s /bin/bash hacker && echo "hacker:hacker" | chpasswd 

# --- Configure SSH ---
RUN mkdir -p /home/hacker/.ssh && \
ssh-keygen -t rsa -b 2048 -f /home/hacker/.ssh/id_rsa -N "" && \
chown -R hacker:hacker /home/hacker/.ssh && \
mkdir /var/run/sshd

# --- Download and Configure Linux Privilege Escalation Tools ---
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/