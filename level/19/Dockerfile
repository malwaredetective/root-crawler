# -----------------------------------------------
# Level: 19
# Difficulty: Medium
# Categories: Git
# Description: The .GIT repo contains sensitive data that was recently removed.
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------

FROM khub/root-crawler-base:latest
LABEL project="root-crawler"

# --- Install Required Software Packages ---
RUN apt-get install -y python3-requests sqlite3

# --- Update Users ---
ARG ROOTPW=onePASSWORDtoRULEthemALL!
RUN echo "root:${ROOTPW}" | chpasswd

# --- Configure Privilege Escalation Vulnerability ---
WORKDIR /opt/simple-vuln-scanner

COPY create-repo.sh /tmp/create-repo.sh
RUN /tmp/create-repo.sh && rm /tmp/create-repo.sh && \
chown -R hacker:hacker /opt/simple-vuln-scanner && \
ln -s /opt/simple-vuln-scanner/main.py /home/hacker/run-scanner

# --- Create the Root Flag ---
RUN echo "f1749beaae51231edd44bb42473f0b73" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD ["/usr/sbin/sshd", "-D"]

