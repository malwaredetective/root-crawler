# -----------------------------------------------
# Level: 14
# Difficulty: Medium
# Categories: SUDO
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Install Required Software Packages ---
RUN apt-get install -y \
    gcc

# --- Configure Privilege Escalation Vulnerability ---
COPY cyber-assistant.c /tmp/cyber-assistant.c
RUN gcc /tmp/cyber-assistant.c -o /usr/local/bin/cyber-assistant -ldl && \
rm /tmp/cyber-assistant.c && \
chmod 755 /usr/local/bin/cyber-assistant && \
echo 'Defaults env_keep += "LD_LIBRARY_PATH"' > /etc/sudoers.d/ld_library_path && \
echo 'hacker ALL=(root) NOPASSWD: /usr/local/bin/cyber-assistant' > /etc/sudoers.d/cyber-assistant && \
chmod 440 /etc/sudoers.d/ld_library_path /etc/sudoers.d/cyber-assistant

# --- Create the Root Flag ---
RUN echo "a623362224d97f447b70ea9dfd13cca4" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
