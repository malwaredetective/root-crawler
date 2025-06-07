# -----------------------------------------------
# Level: 9
# Difficulty: Easy
# Categories: SSH, Weak File Permissions
# Description: The user can create an SSH key to another user. The other used can execute a GTFOBIN as SUDO.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Create Users ---
# 1. Grants 'zerocool' passwordless sudo access to /usr/bin/nano via a dedicated sudoers file.
RUN useradd -m -s /bin/bash zerocool && echo "zerocool:neverlucky!" | chpasswd && \ 
echo "zerocool ALL=(ALL) NOPASSWD: /usr/bin/nano" >> /etc/sudoers.d/zerocool-nano && chmod 440 /etc/sudoers.d/zerocool-nano 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Sets up an SSH keypair for the 'hacker' user:
# 2. Makes /home/zerocool world-accessible (chmod 755):
# 3. Proper permissions are set on the .ssh directory and authorized_keys to simulate a real environment,
# 4. Copies the vim binary to /home/hacker/vim.
# 5. Changes ownership to 'zerocool' and sets the SUID bit (chmod 4755):
RUN mkdir -p /home/hacker/.ssh && \
ssh-keygen -t rsa -b 2048 -f /home/hacker/.ssh/id_rsa -N "" && \
chown -R hacker:hacker /home/hacker/.ssh && \
chmod 755 /home/zerocool && \
mkdir -p /home/zerocool/.ssh && \
touch /home/zerocool/.ssh/authorized_keys && \
chmod 700 /home/zerocool/.ssh && \
chmod 600 /home/zerocool/.ssh/authorized_keys && \
chown -R zerocool:zerocool /home/zerocool/.ssh && \
cp /usr/bin/vim /home/hacker/vim && \
chown zerocool:zerocool /home/hacker/vim && \
chmod 4755 /home/hacker/vim && \
echo "If you want to be a real linux guru, than you HAVE to use vim! Stop using nano like a script kiddie. I set you up some challenges on my home drive. Try working through them when you get a chance." > /home/hacker/note.txt && \
chown hacker:hacker /home/hacker/note.txt && chmod 644 /home/hacker/note.txt && \
echo "Welcome to the VIM Challenges!\n" > /home/zerocool/vim_challenges.txt && \
echo "1. Open this file in vim and go to line 10." >> /home/zerocool/vim_challenges.txt && \
echo "2. Search for the word 'sudo' in this file." >> /home/zerocool/vim_challenges.txt && \
echo "3. Replace the word 'hacker' with your username throughout this file using vim commands." >> /home/zerocool/vim_challenges.txt && \
echo "4. Use visual mode to select and copy a block of text." >> /home/zerocool/vim_challenges.txt && \
echo "5. Set a mark on line 5 and jump to it." >> /home/zerocool/vim_challenges.txt && \
echo "" >> /home/zerocool/vim_challenges.txt && \
echo "Bonus: Use vim's shell mode to run 'whoami' from inside vim." >> /home/zerocool/vim_challenges.txt && \
echo "" >> /home/zerocool/vim_challenges.txt && \
echo "Remember: Real hackers don't use nano." >> /home/zerocool/vim_challenges.txt && \
chown zerocool:zerocool /home/zerocool/vim_challenges.txt && \
chmod 644 /home/zerocool/vim_challenges.txt

# --- Create the Root Flag ---
RUN echo "144f541844236aaac836ae692552c262" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]