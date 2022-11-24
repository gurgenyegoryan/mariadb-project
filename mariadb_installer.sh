#!/bin/bash

# Install mariadb server
apt install mariadb-server -y
service mariadb start

DEBIAN_FRONTEND=noninteractive apt-get -yq install expect


MYSQL_ROOT_PASSWORD=Yeg.1995

SECURE_MYSQL=$(expect -c "
set timeout 10
spawn mysql_secure_installation
expect \"Enter current password for root (enter for none):\"
send \"$MYSQL\r\"
expect \"Switch to unix_socket authentication?\"
send \"n\r\"
expect \"Change the root password?\"
send \"y\r\"
expect \"New Password?\"
send \"Yeg.1995\r\"
expect \"Retype password\"
send \"Yeg.1995\r\"
expect \"Disallow root login remotely?\"
send \"n\r\"
expect \"Remove test database and access to it?\"
send \"y\r\"
expect \"Reload privilege tables now?\"
send \"y\r\"
expect eof
")

echo "$SECURE_MYSQL"



mysql -e "CREATE DATABASE pythontest /*\!40100 DEFAULT CHARACTER SET utf8 */;"
mysql -e "GRANT ALL PRIVILEGES ON pythontest.* TO 'root'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"
