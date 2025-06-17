# -----------------------------------------------
# Level: 9
# Difficulty: Medium
# Categories: SSH, Weak File Permissions
# Description: The user can create an SSH key to another user. The other used can execute a GTFOBIN as SUDO.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Create Users ---
# 1. Grants 'zerocool' passwordless sudo access to /usr/bin/nano via a dedicated sudoers file.
RUN useradd -m -s /bin/bash zerocool && echo "zerocool:neverlucky!" | chpasswd && \ 
echo "zerocool ALL=(ALL) NOPASSWD: /usr/bin/nano" >> /etc/sudoers.d/zerocool-nano && chmod 440 /etc/sudoers.d/zerocool-nano 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Makes /home/zerocool world-accessible (chmod 755) and pre-configures SSH.
# 2. Copies the vim binary to /home/hacker/vim with SUID as Zerocool.
# 3. Adds SUDO GTFObin for Zerocool.
COPY vim_challenges.txt /home/zerocool/vim_challenges.txt
RUN chmod 755 /home/zerocool && \
mkdir -p /home/zerocool/.ssh && \
touch /home/zerocool/.ssh/authorized_keys && \
chmod 700 /home/zerocool/.ssh && \
chmod 600 /home/zerocool/.ssh/authorized_keys && \
chown -R zerocool:zerocool /home/zerocool/.ssh && \
cp /usr/bin/vim /home/hacker/vim && \
chown zerocool:zerocool /home/hacker/vim && \
chmod 4755 /home/hacker/vim && \
echo "If you want to be a real linux guru, than you HAVE to use vim! Stop using nano like a script kiddie. I set you up some challenges on my home drive. Try working through them when you get a chance.\n\n- Zerocool" > /home/hacker/note.txt && \
chown hacker:hacker /home/hacker/note.txt && chmod 644 /home/hacker/note.txt && \
chown zerocool:zerocool /home/zerocool/vim_challenges.txt && chmod 644 /home/zerocool/vim_challenges.txt

# --- Create the Root Flag ---
RUN echo "144f541844236aaac836ae692552c262" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]