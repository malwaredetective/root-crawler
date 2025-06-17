# -----------------------------------------------
# Level: 10
# Difficulty: Easy
# Categories: SSH, Weak File Permissions
# Description: Hacker can use a SUID copy of cat to read root's private SSH key and login as root.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Configure Privilege Escalation Vulnerability ---
# 1. Create a custom SUID binary: /usr/local/bin/supercat
RUN mkdir -p /root/.ssh && \
chmod 700 /root/.ssh && \
ssh-keygen -t rsa -b 2048 -f /root/.ssh/id_rsa -N "" && \
cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys && \
chmod 600 /root/.ssh/authorized_keys && \
cp /bin/cat /usr/local/bin/supercat && \
chown root:root /usr/local/bin/supercat && \
chmod 4755 /usr/local/bin/supercat && \
chmod 755 /home/hacker

# --- Create the Root Flag ---
RUN echo "Hmm ... Isn't there normally a flag here?" > /root/root.txt && chmod 400 /root/root.txt 
RUN echo "6430891943122750375619a89b596833" > /root/hidden-flag.txt && chmod 400 /root/hidden-flag.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
