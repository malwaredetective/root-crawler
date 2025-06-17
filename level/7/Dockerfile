# -----------------------------------------------
# Level: 7
# Difficulty: Medium
# Categories: Capabilities
# Description: The user can escalate privileges due to a binary with misconfigured capabilities.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Create Users ---
RUN useradd -m -s /bin/bash tav && echo "tav:thedarkurge" | chpasswd && \
useradd -m -s /bin/bash shadowheart && echo "shadowheart:shadowcutie" | chpasswd && \
useradd -m -s /bin/bash laezel && echo "laezel:baezel" | chpasswd && \
useradd -m -s /bin/bash astarion && echo "astarion:bloodsucker" | chpasswd

# --- Configure Privilege Escalation Vulnerability ---
# 1. Assigns the 'cap_setuid+ep' capability to the system Python3 binary (/usr/bin/python3).

COPY character_sheet.py /home/hacker/character_sheet.py
COPY Tav.txt /home/tav/character_sheet.md
COPY Astarion.txt /home/astarion/character_sheet.md
COPY Laezel.txt /home/laezel/character_sheet.md
COPY Shadowheart.txt /home/shadowheart/character_sheet.md

RUN  dos2unix /home/hacker/character_sheet.py && \
chown hacker:hacker /home/hacker/character_sheet.py && \
chmod 755 /home/hacker/character_sheet.py && \
chown tav:tav /home/tav/character_sheet.md && \
chmod 755 /home/tav/character_sheet.md && \
chown astarion:astarion /home/astarion/character_sheet.md && \
chmod 755 /home/astarion/character_sheet.md && \
chown laezel:laezel /home/laezel/character_sheet.md && \
chmod 755 /home/laezel/character_sheet.md && \
chown shadowheart:shadowheart /home/shadowheart/character_sheet.md && \
chmod 755 /home/shadowheart/character_sheet.md && \
setcap cap_setuid+ep $(readlink -f /usr/bin/python3)

# --- Create the Root Flag ---
RUN echo "49f17dbc98399bf6b9753487b48a6ff3" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]