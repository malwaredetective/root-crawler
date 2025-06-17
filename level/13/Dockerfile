# -----------------------------------------------
# Level: 13
# Difficulty: Medium
# Categories: SUDO
# Description: The user can exploit a vulnerable SUDO configuration with LD_PRELOAD.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get install -y \
    gcc

# --- Configure Privilege Escalation Vulnerability ---
# 1. Copies a custom C program (hacker-motd.c) into the container and compiles it to /usr/local/bin/hacker-motd.
# 2. The sudoers file for 'hacker' keeps the LD_PRELOAD environment variable when running /usr/local/bin/hacker-motd as root.
COPY hacker-motd.c /tmp/hacker-motd.c
RUN gcc /tmp/hacker-motd.c -o /usr/local/bin/hacker-motd && \
rm /tmp/hacker-motd.c && \
chmod 755 /usr/local/bin/hacker-motd && \
echo 'Defaults env_keep += "LD_PRELOAD"' > /etc/sudoers.d/ld_preload && \
echo 'hacker ALL=(root) NOPASSWD: /usr/local/bin/hacker-motd' > /etc/sudoers.d/hacker-motd && \
chmod 440 /etc/sudoers.d/ld_preload /etc/sudoers.d/hacker-motd

# --- Create the Root Flag ---
RUN echo "29a23565f022a110bc2b895c7ddd2d75" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
