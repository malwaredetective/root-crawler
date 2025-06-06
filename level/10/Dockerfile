# -----------------------------------------------
# Level: 10
# Difficulty: Easy
# Categories: SSH, Weak File Permissions
# Description: Hacker can use a SUID copy of cat to read root's private SSH key and login as root.
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
mkdir /var/run/sshd

# --- Download and Configure Linux Privilege Escalation Tools ---
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/

# --- Configure Privilege Escalation Vulnerability ---
RUN mkdir -p /root/.ssh && \
chmod 700 /root/.ssh && \
ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -N "" && \
cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys && \
chmod 600 /root/.ssh/authorized_keys && \
cp /bin/cat /home/hacker/supercat && \
chown root:root /home/hacker/supercat && \
chmod 4755 /home/hacker/supercat && \
chmod 755 /home/hacker

# --- Create the Root Flag ---
RUN echo "Hmm ... Isn't there normally a flag here?" > /root/root.txt && chmod 400 /root/root.txt 
RUN echo "6430891943122750375619a89b596833" > /root/hidden-flag.txt && chmod 400 /root/hidden-flag.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
