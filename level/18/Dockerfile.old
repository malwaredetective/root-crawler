# -----------------------------------------------
# Level: 18
# Difficulty: 
# Categories: CVE
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

#FROM ubuntu:18.04
FROM khub/root-crawler:latest
ENV DEBIAN_FRONTEND=noninteractive

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    make \
    net-tools \
    netcat-openbsd \
    libpam0g-dev \
    libutempter0 \
    libutempter-dev \
    libncurses-dev 

# --- Configure Privilege Escalation Vulnerability ---
WORKDIR /tmp
COPY screen-4.5.0.tar.gz /tmp/screen-4.5.0.tar.gz

RUN tar xzf screen-4.5.0.tar.gz && \
cd screen-4.5.0 && \
./configure CFLAGS="-fcommon" && \
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

