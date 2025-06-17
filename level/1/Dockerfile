# -----------------------------------------------
# Level: 1
# Difficulty: Medium
# Categories: SUDO
# Description: The instance is running a vulnerable version of SUDO.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-legacy:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    libssl-dev \
    libpam0g-dev 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Extract and compile sudo 1.8.27, which is known to be vulnerable to CVE-2019-14287.
# 2. Update the sudoers file to allow 'hacker' user to execute /usr/bin/vim as any user except root, without a password.
COPY sudo-1.8.27.tar.gz /tmp/
WORKDIR /tmp
RUN tar xzf sudo-1.8.27.tar.gz && \
cd /tmp/sudo-1.8.27 && \
./configure && make && make install && \
rm -rf /tmp/* && \
echo 'hacker ALL=(ALL,!root) NOPASSWD: /usr/bin/vim' >> /etc/sudoers 

# --- Create the Root Flag ---
RUN echo "739d80f289f091f1d5faf12cfd25fe83" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
