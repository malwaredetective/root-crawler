# -----------------------------------------------
# Level: 15
# Difficulty: Medium
# Categories: CVE
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM ubuntu:22.04

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    sudo \
    openssh-server \
    build-essential \
    vim \
    nano \
    file \
    cron \
    perl \
    djvulibre-bin 

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
COPY exiftool-12.23.zip /tmp/exiftool-12.23.zip
RUN cd /tmp && unzip exiftool-12.23.zip && cd exiftool-12.23 && \
    perl Makefile.PL && make && make test && make install && \
    cd / && rm -rf /tmp/exiftool-12.23 /tmp/exiftool-12.23.zip

COPY secret-message.png /home/hacker/secret-message.png
COPY iGIVEup.py /usr/local/bin/iGIVEup.py
RUN echo "Can you find the hidden message within secret-message.png? We have reason to believe that hackers were somehow adding additional data to this file to communicate in secret.\n\nIf you get can't solve it, find the iGIVEup.py script to admit defeat!" > /home/hacker/challenge.txt && \
chown hacker:hacker /home/hacker/challenge.txt && \
chown hacker:hacker /home/hacker/secret-message.pngs && \
chown root:root /usr/local/bin/iGIVEup.py && chmod 755 /usr/local/bin/iGIVEup.py && \
echo 'hacker ALL=(root) NOPASSWD: /usr/bin/python3 /usr/local/bin/iGIVEup.py' > /etc/sudoers.d/hacker-iGIVEup && \
chmod 440 /etc/sudoers.d/hacker-iGIVEup

# --- Create the Root Flag ---
RUN echo "815825d292b7c79656b61b5917b49e9b" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
