# -----------------------------------------------
# Level: 1
# Difficulty: Hard
# Categories: SUDO, CVE
# Description: The instance is running a vulnerable version of SUDO.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM ubuntu:18.04

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    gcc \ 
    make \ 
    build-essential \
    libssl-dev \
    libpam0g-dev \
    openssh-server \
    vim \
    nano \
    file \
    cron

# --- Create Users ---
RUN useradd -m -s /bin/sh hacker && echo "hacker:hacker" | chpasswd && \
mkdir /var/run/sshd

# Download and Configure Linux Privilege Escalation Tools
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/

# --- Configure Privilege Escalation Vulnerability ---
WORKDIR /opt
COPY sudo-1.8.27.tar.gz /opt/
RUN tar xzf sudo-1.8.27.tar.gz && \
    cd sudo-1.8.27 && \
    ./configure && \
    make && \
    make install && \
    echo 'hacker ALL=(ALL,!root) NOPASSWD: /usr/bin/vim' >> /etc/sudoers

# --- Create the Root Flag ---
RUN echo "739d80f289f091f1d5faf12cfd25fe83" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
