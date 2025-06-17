# -----------------------------------------------
# Level: 5
# Difficulty: Easy
# Categories: SUDO, Lateral Movement, GTFOBins
# Description: .bash_history leaks password information for another user. The other used can execute a GTFOBIN as SUDO.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Create Users ---
RUN useradd -m -s /bin/bash neo && echo "neo:hackersRUNonCOFFEE!" | chpasswd

# --- Configure Privilege Escalation Vulnerability ---
# 1. The hacker's .bash_history contains a plaintext password for the 'neo' user (hackersRUNonCOFFEE!)
# 2. Creates a file in /etc/sudoers.d/ allowing 'neo' to run /usr/bin/find as root without a password.
RUN echo "ls -la\nwhoami\nsu hackersRUNonCOFFEE!\nsu neo\nexit" > /home/hacker/.bash_history && \
chown hacker:hacker /home/hacker/.bash_history && \
chmod 600 /home/hacker/.bash_history && \
echo "neo ALL=(ALL) NOPASSWD: /usr/bin/find" > /etc/sudoers.d/neo-find && \
chmod 440 /etc/sudoers.d/neo-find

# --- Create the Root Flag ---
RUN echo "d216d3c4b24304fc4674c728c2ececf4" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]