# -----------------------------------------------
# Level: 3
# Difficulty: Easy
# Categories: Weak File Permissions
# Description: /etc/shadow is writeable.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get install -y whois 

# --- Create Users ---
RUN useradd -m -s /bin/bash swiper && echo "swiper:swiperNOswiping!" | chpasswd 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Sets /etc/shadow permissions to 666 (world-writable), which is highly insecure.
# 2. Create a cronjob that resets the root users password, adding a race condition when the player updates the root users password.
# 3. Added a MOTD for comidic effect. 
COPY reset-password.sh /root/reset-password.sh

RUN chmod 666 /etc/shadow && \
echo '* * * * * root /root/reset-password.sh' >> /etc/crontab && \
chmod 700 /root/reset-password.sh && \
echo "\
******************************************************\n\
*            !!! WARNING FROM THE ADMIN !!!          *\n\
*                                                    *\n\
*   To all you pathetic low-privilege users:         *\n\
*   STOP changing my password!                       *\n\
*                                                    *\n\
*   I’ve upgraded my defenses, so your feeble        *\n\
*   attempts accomplish NOTHING in the end.          *\n\
*                                                    *\n\
*   I won't reveal my secret weapon, but             *\n\
*   unless you're quicker than a caffeinated         *\n\
*   squirrel, give up now!                           *\n\
*                                                    *\n\
*   If you thought you could outsmart me,            *\n\
*   think again!                                     *\n\
******************************************************" > /etc/motd


# --- Create the Root Flag ---
RUN echo "370b6eb5bc21ff135c9a92c371c4f422" > /root/root.txt && chmod 400 /root/root.txt

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD service cron start && /usr/sbin/sshd -D
