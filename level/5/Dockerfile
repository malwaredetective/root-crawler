# -----------------------------------------------
# Level: 5
# Difficulty: Easy
# Categories: SUDO, Lateral Movement, GTFOBins
# Description: .bash_history leaks password information for another user. The other used can execute a GTFOBIN as SUDO.
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
    cron

# --- Create Users ---
RUN useradd -m -s /bin/bash hacker && echo "hacker:hacker" | chpasswd && \
useradd -m -s /bin/bash neo && echo "neo:hackersRUNonCOFFEE!" | chpasswd && \
mkdir /var/run/sshd

# --- Download and Configure Linux Privilege Escalation Tools ---  
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/

# --- Configure Privilege Escalation Vulnerability ---
RUN echo -e "ls -la\nwhoami\nsu hackersRUNonCOFFEE!\nsu neo\nexit" > /home/hacker/.bash_history && \
chown hacker:hacker /home/hacker/.bash_history && \
chmod 600 /home/hacker/.bash_history && \
echo "neo ALL=(ALL) NOPASSWD: /usr/bin/find" > /etc/sudoers.d/neo-find && \
chmod 440 /etc/sudoers.d/neo-find

# --- Create the Root Flag ---
RUN echo "d216d3c4b24304fc4674c728c2ececf4" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]