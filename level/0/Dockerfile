# -----------------------------------------------
# Level: 0
# Difficulty: Easy
# Categories: SUDO
# Description: The user can escalate their privileges by moving laterally to another accout with a hidden SUID bash binary owned by root.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get install -y \
    unzip \
    bzip2 \
    zip \
    p7zip-full

# --- Create Users ---
RUN useradd -m -s /bin/bash jigsaw && echo "jigsaw:theTRUTHwillsetyoufree" | chpasswd 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Create an archive puzzle in hacker's home directory.
# 2. Setup a hidden SUID bash binary within jigsaw's home directory.
WORKDIR /tmp
RUN  echo "theTRUTHwillsetyoufree" > /tmp/iwant2playagame && \
zip iwant2playagame.zip iwant2playagame && \
tar -cf iwant2playagame.zip.tar iwant2playagame.zip && \
gzip iwant2playagame.zip.tar && \
bzip2 iwant2playagame.zip.tar.gz && \
7z a iwant2playagame.7z iwant2playagame.zip.tar.gz.bz2 && \
mv iwant2playagame.7z /home/hacker/iwant2playagame && \
rm -rf /tmp/* && \
chown hacker:hacker /home/hacker/iwant2playagame && \
echo "jigsaw ALL=(ALL) NOPASSWD: /usr/bin/ls" > /etc/sudoers.d/jigsaw-ls && \
chmod 440 /etc/sudoers.d/jigsaw-ls && \
mkdir /home/jigsaw/.hidden && \
cp /bin/bash /home/jigsaw/.hidden/rootbash && \
chmod +s /home/jigsaw/.hidden/rootbash 

# --- Create the Root Flag ---
RUN echo "207eeec707affb4ab39ffb63dc3df9e8" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]