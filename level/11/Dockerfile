# -----------------------------------------------
# Level: 11
# Difficulty: Easy
# Categories:  SSH, Password Cracking
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
ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -N "ugotpwned" && \
cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys && \
chmod 600 /root/.ssh/id_rsa /root/.ssh/authorized_keys && \
cp /root/.ssh/id_rsa /home/hacker/root.key && \
chown hacker:hacker /home/hacker/root.key && \
chmod 400 /home/hacker/root.key && \
echo -e "Hey,\n\nYou can use the private key 'root.key' to log into the database server as root and troubleshoot the error we've been getting.\nThe passphrase is the one we always use. Let me know if you find anything!\n" > /home/hacker/note.txt && \
chown hacker:hacker /home/hacker/note.txt && \
chmod 644 /home/hacker/note.txt

# --- Create the Root Flag ---
RUN echo "d87f33aad39073e70d184d10ddb6562b" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
