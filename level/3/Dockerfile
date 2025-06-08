# -----------------------------------------------
# Level: 3
# Difficulty: Easy
# Categories: Weak File Permissions
# Description: /etc/shadow is writeable.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest

# --- Configure Privilege Escalation Vulnerability ---
# 1. Sets /etc/shadow permissions to 666 (world-writable), which is highly insecure.
# 2. Any user on the system, including 'hacker', can directly modify the password hashes stored in /etc/shadow. An attacker can replace the root hash with a known value, or add a new user with root privileges,
RUN chmod 666 /etc/shadow

# --- Create the Root Flag ---
RUN echo "370b6eb5bc21ff135c9a92c371c4f422" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
