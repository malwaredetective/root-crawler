# -----------------------------------------------
# Level: 7
# Difficulty: Easy
# Categories: Capabilities
# Description: The user can escalate privileges due to a binary with misconfigured capabilities.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Configure Privilege Escalation Vulnerability ---
# 1. Assigns the 'cap_setuid+ep' capability to the system Python3 binary (/usr/bin/python3).
RUN setcap cap_setuid+ep $(readlink -f /usr/bin/python3)

# --- Create the Root Flag ---
RUN echo "49f17dbc98399bf6b9753487b48a6ff3" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]