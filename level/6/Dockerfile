# -----------------------------------------------
# Level: 6
# Difficulty: Easy
# Categories: SUDO, GTFOBins
# Description: The user can escalate privileges due to a GTFOBin.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Install Required Software Packages ---
RUN apt-get install -y \
    gcc

# --- Configure Privilege Escalation Vulnerability ---
# 1. Grants the 'hacker' user passwordless sudo access to /usr/bin/gcc.
RUN echo "hacker ALL=(ALL) NOPASSWD: /usr/bin/gcc" >> /etc/sudoers

# --- Create the Root Flag ---
RUN echo "8ee7c23a901076e22e8b6ec407c190fd" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]