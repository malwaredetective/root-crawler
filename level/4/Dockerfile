# -----------------------------------------------
# Level: 4
# Difficulty: Easy
# Categories: Weak File Permissions
# Description: /etc/passwd is writeable.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Configure Privilege Escalation Vulnerability ---
# 1. Set permissions on /etc/passwd to 666 (world-writable), which is extremely insecure.
RUN chmod 666 /etc/passwd

# --- Create the Root Flag ---
RUN echo "b93841e55f11579f2203690ce64be128" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
