# -----------------------------------------------
# Level: 15
# Difficulty: Medium
# Categories: CVE
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest

# --- Install Required Software Packages ---
RUN apt-get install -y \
    build-essential \
    perl \
    djvulibre-bin 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Installs a vulnerable version of exiftool (12.23), which is affected by CVE-2021-22204 (RCE via crafted DjVu files).
# 2. Provides a mysterious PNG for the user to analyze, with challenge instructions.
# 3. Adds an "I give up" script for the user to run via sudo if they want to skip the exploit.

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
