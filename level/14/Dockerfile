# -----------------------------------------------
# Level: 14
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

# --- Download and Configure Linux Privilege Escalation Tools ---
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/

# --- Configure Privilege Escalation Vulnerability ---
# Copy and compile cyber-assistant
COPY cyber-assistant.c /tmp/cyber-assistant.c
RUN gcc /tmp/cyber-assistant.c -o /usr/local/bin/cyber-assistant -ldl && \
    rm /tmp/cyber-assistant.c && \
    chmod 755 /usr/local/bin/cyber-assistant && \
    echo 'Defaults env_keep += "LD_LIBRARY_PATH"' > /etc/sudoers.d/ld_library_path && \
    echo 'hacker ALL=(root) NOPASSWD: /usr/local/bin/cyber-assistant' > /etc/sudoers.d/cyber-assistant && \
    chmod 440 /etc/sudoers.d/ld_library_path /etc/sudoers.d/cyber-assistant

# --- Create the Root Flag ---
RUN echo "a623362224d97f447b70ea9dfd13cca4" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
