# -----------------------------------------------
# Level: 2
# Difficulty: Medium
# Categories: Weak File Permissions; Password Cracking
# Description: /etc/shadow is readable; The root password is crackable.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Configure Privilege Escalation Vulnerability ---
# 1. Sets the root password to a hash of 'masterhacker', making it susceptible to password cracking attacks.
# 2. Changes permissions on /etc/shadow to 644, making it world-readable.
RUN echo "root:$(openssl passwd -6 masterhacker)" | chpasswd && \
chmod 644 /etc/shadow

# --- Create the Root Flag ---
RUN echo "0e818a27a3fea74347a605528f334e3f" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
