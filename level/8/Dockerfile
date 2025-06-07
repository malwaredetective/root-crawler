# -----------------------------------------------
# Level: 8
# Difficulty: Easy
# Categories: Capabilities
# Description: The user can escalate privileges due to a binary with misconfigured capabilities.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler:latest

# --- Install Required Software Packages ---
RUN apt-get install -y \
    gdb

# --- Configure Privilege Escalation Vulnerability ---
# 1. Assigns the 'cap_setuid+ep' capability to the /usr/bin/gdb binary (GNU Debugger).
RUN setcap cap_setuid+ep /usr/bin/gbd

# --- Create the Root Flag ---
RUN echo "93b02d0e7fee22a6efd60585989ccdcd" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]
