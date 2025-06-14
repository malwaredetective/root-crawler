# -----------------------------------------------
# Level: 8
# Difficulty: Easy
# Categories: Capabilities
# Description: The user can escalate privileges due to a binary with misconfigured capabilities.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest

# --- Install Required Software Packages ---
RUN apt-get install -y \
    gdb \
    libcap2-bin \
    gcc

# --- Configure Privilege Escalation Vulnerability ---
# 1. Assigns the 'cap_setuid+ep' capability to the /usr/bin/gdb binary (GNU Debugger).
COPY crackme.c /root/crackme.c

RUN setcap cap_setuid+ep /usr/bin/gdb  && \
gcc /root/crackme.c -o /home/hacker/crackme && \
chown hacker:hacker /home/hacker/crackme && \
echo "Can you reverse engineer this classic 'crackme' challenge and get the flag?" > /home/hacker/challenge.txt && \
chown hacker:hacker /home/hacker/challenge.txt && \
ln -s /usr/bin/gdb /home/hacker/gdb && chown -h hacker:hacker /home/hacker/gdb && \
rm /root/crackme.c 

# --- Solving the Crack Me Challenge ---
# Open the crackme binary within GDB
# break main
# run
# disas main (Identify the Address of the STRCMP function)
# break *0xHEX_ADDRESS (break *0x584c1770b100)
# continue
# [When prompted, input an invalid password]
# stepi
# finish
# set $eax=0 (Trick the binary into thinking the correct password was submitted)
# continue

# --- Create the Root Flag ---
RUN echo "93b02d0e7fee22a6efd60585989ccdcd" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
