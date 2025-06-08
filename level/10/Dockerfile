# -----------------------------------------------
# Level: 10
# Difficulty: Easy
# Categories: SSH, Weak File Permissions
# Description: Hacker can use a SUID copy of cat to read root's private SSH key and login as root.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest

# --- Configure Privilege Escalation Vulnerability ---
# This block sets up the core privilege escalation path for the user:
# 1. Generates a root-owned SSH keypair in /root/.ssh.
# 2. Creates a SUID-root copy of /bin/cat named 'supercat' in /home/hacker.
# 3. Sets /home/hacker permissions to 755 to ensure 'hacker' can execute the SUID binary.
RUN mkdir -p /root/.ssh && \
chmod 700 /root/.ssh && \
ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -N "" && \
cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys && \
chmod 600 /root/.ssh/authorized_keys && \
cp /bin/cat /home/hacker/supercat && \
chown root:root /home/hacker/supercat && \
chmod 4755 /home/hacker/supercat && \
chmod 755 /home/hacker

# --- Create the Root Flag ---
RUN echo "Hmm ... Isn't there normally a flag here?" > /root/root.txt && chmod 400 /root/root.txt 
RUN echo "6430891943122750375619a89b596833" > /root/hidden-flag.txt && chmod 400 /root/hidden-flag.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
