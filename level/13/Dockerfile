# -----------------------------------------------
# Level: 13
# Difficulty: Medium
# Categories: SUDO
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
    gcc

# --- Create Users ---
RUN useradd -m -s /bin/bash hacker && echo "hacker:hacker" | chpasswd && \
mkdir /var/run/sshd

# Download and Configure Linux Privilege Escalation Tools  
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/

# --- Configure Privilege Escalation Vulnerability ---
COPY hacker-motd.c /tmp/hacker-motd.c
RUN gcc /tmp/hacker-motd.c -o /usr/local/bin/hacker-motd && \
    rm /tmp/hacker-motd.c && \
    chmod 755 /usr/local/bin/hacker-motd && \
    echo 'Defaults env_keep += "LD_PRELOAD"' > /etc/sudoers.d/ld_preload && \
    echo 'hacker ALL=(root) NOPASSWD: /usr/local/bin/hacker-motd' > /etc/sudoers.d/hacker-motd && \
    chmod 440 /etc/sudoers.d/ld_preload /etc/sudoers.d/hacker-motd

# --- Create the Root Flag ---
RUN echo "29a23565f022a110bc2b895c7ddd2d75" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
