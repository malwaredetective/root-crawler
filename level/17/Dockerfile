# -----------------------------------------------
# Level: 17
# Difficulty: 
# Categories: 
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------
    
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# --- Install Required Software Packages ---
RUN apt-get update && apt-get install -y \
    openssh-server \
    vim \
    nano \
    file \
    cron \
    apache2 \
    php \
    unzip \
    netcat \
    net-tools

# --- Create Users ---
RUN useradd -m -s /bin/bash hacker && echo "hacker:hacker" | chpasswd && \
echo 'root:$uper$ecureP@55w0rd!123' | chpasswd && \
mkdir /var/run/sshd

# --- Download and Configure Linux Privilege Escalation Tools ---
RUN mkdir /opt/tools && \
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -O /opt/tools/linpeas.sh && \
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -O /opt/tools/lse.sh && \
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 -O /opt/tools/pspy64 && \
chown -R hacker:hacker /opt/tools/ && \
chmod -R 755 /opt/tools/

# --- Configure Privilege Escalation Vulnerability ---

# Allow password authentication and root login over SSH (for CTF/demo)
RUN sed -i 's/^#*PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#*PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    echo "AllowUsers hacker root" >> /etc/ssh/sshd_config

# Set up Apache
RUN echo "ServerName root-crawler-wordpress.local" >> /etc/apache2/apache2.conf

# "Install" WordPress (just extract, no DB)
COPY wordpress-6.8.1.tar.gz /
RUN tar -xzf /wordpress-6.8.1.tar.gz -C /var/www/html/ && \
cp -r /var/www/html/wordpress/* /var/www/html/ && \
rm -rf /var/www/html/wordpress* /wordpress-6.8.1.tar.gz && \
chown -R www-data:www-data /var/www/html/ && \
chmod -R 755 /var/www/html/ && \
mkdir -p /var/www/html/wp-content/plugins/webshell-plugin

COPY webshell.php /var/www/html/wp-content/plugins/webshell-plugin/webshell.php
RUN chown -R www-data:www-data /var/www/html/wp-content/plugins/webshell-plugin

COPY wp-config.php /var/www/html/wp-config.php
RUN chown www-data:www-data /var/www/html/wp-config.php && chmod 640 /var/www/html/wp-config.php && \
echo "I've already established a foothold as www-data here: http://localhost/wp-content/plugins/webshell-plugin/webshell.php?cmd=id\n\nI just need you to finish the job.\n\n- malwaredetective" > /home/hacker/pwned.txt && chown hacker:hacker /home/hacker/pwned.txt

# --- Create the Root Flag ---
RUN echo "78c994e2cba1dc7531dd1bbe30de7583" > /root/root.txt && chmod 400 /root/root.txt 

# SSH setup
RUN mkdir /var/run/sshd

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD service ssh start && apache2ctl -D FOREGROUND
