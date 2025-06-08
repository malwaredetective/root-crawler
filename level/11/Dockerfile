# -----------------------------------------------
# Level: 11
# Difficulty: Easy
# Categories:  SSH, Password Cracking
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest

# --- Configure Privilege Escalation Vulnerability ---
# 1. Generates a root-owned SSH keypair in /root/.ssh with passphrase 'ugotpwned'.
# 2. Copies the root private key (still encrypted/protected by its passphrase) to /home/hacker/root.key,
# 3. Includes a note to the hacker, hinting that the private key is for "the database server as root"
# 4. The user can now attempt to crack the private key passphrase (e.g., with John the Ripper or ssh2john.py),
RUN mkdir -p /root/.ssh && \
chmod 700 /root/.ssh && \
ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -N "ugotpwned" && \
cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys && \
chmod 600 /root/.ssh/id_rsa /root/.ssh/authorized_keys && \
cp /root/.ssh/id_rsa /home/hacker/root.key && \
chown hacker:hacker /home/hacker/root.key && \
chmod 400 /home/hacker/root.key && \
echo -e "Hey,\n\nYou can use the private key 'root.key' to log into the database server as root and troubleshoot the error we've been getting.\nThe passphrase is the one we always use. Let me know if you find anything!\n" > /home/hacker/note.txt && \
chown hacker:hacker /home/hacker/note.txt && \
chmod 644 /home/hacker/note.txt

# --- Create the Root Flag ---
RUN echo "d87f33aad39073e70d184d10ddb6562b" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
