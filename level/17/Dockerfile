# -----------------------------------------------
# Level: 17
# Difficulty: 
# Categories: 
# Description: 
# Author: malwaredetective
# Last updated: 06/01/2025
# -----------------------------------------------
    
FROM khub/root-crawler-base:latest
LABEL project="root-crawler"
ENV DEBIAN_FRONTEND=noninteractive

# --- Install Required Software Packages ---
RUN apt-get install -y \
    apache2 \
    php \
    unzip \
    netcat \
    net-tools

# --- Create Users ---
RUN echo 'root:$uper$ecureP@55w0rd!123' | chpasswd 

# --- Configure Privilege Escalation Vulnerability ---
# 1. Set up Apache
# 2. Simulate a functional WordPress installation (Kinda :P)
COPY wordpress-6.8.1.tar.gz /
RUN tar -xzf /wordpress-6.8.1.tar.gz -C /var/www/html/ && \
cp -r /var/www/html/wordpress/* /var/www/html/ && \
rm -rf /var/www/html/wordpress* /wordpress-6.8.1.tar.gz && \
chown -R www-data:www-data /var/www/html/ && \
chmod -R 755 /var/www/html/ && \
echo "ServerName root-crawler-wordpress.local" >> /etc/apache2/apache2.conf && \ 
mkdir -p /var/www/html/wp-content/plugins/webshell-plugin

COPY webshell.php /var/www/html/wp-content/plugins/webshell-plugin/webshell.php
RUN chown -R www-data:www-data /var/www/html/wp-content/plugins/webshell-plugin

COPY wp-config.php /var/www/html/wp-config.php
RUN chown www-data:www-data /var/www/html/wp-config.php && chmod 640 /var/www/html/wp-config.php && \
echo "I've already established a foothold as www-data here: http://localhost/wp-content/plugins/webshell-plugin/webshell.php?cmd=id\n\nI just need you to finish the job.\n\n- malwaredetective" > /home/hacker/pwned.txt && chown hacker:hacker /home/hacker/pwned.txt

# --- Create the Root Flag ---
RUN echo "78c994e2cba1dc7531dd1bbe30de7583" > /root/root.txt && chmod 400 /root/root.txt 

# --- Expose SSH port ---
EXPOSE 22

# --- Set the Default Command when the Container Starts ---
CMD service ssh start && apache2ctl -D FOREGROUND
