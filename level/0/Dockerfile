# -----------------------------------------------
# Level: 0
# Difficulty: Easy
# Categories: SUDO
# Description: The user can escalate privileges due to an unsafe sudoers configuration.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Configure Privilege Escalation Vulnerability ---
# 1. Add 'hacker' to the 'sudo' group.
# 2. Set up passwordless sudo for 'hacker' via /etc/sudoers.d/hacker.
RUN adduser hacker sudo && \
    echo "hacker ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/hacker

# --- Create the Root Flag ---
RUN echo "207eeec707affb4ab39ffb63dc3df9e8" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]