#!/bin/bash

function removeGitFiles() {
	rm -fr .git
	rm -f .gitignore
	rm -f README.md
	rm -f package-lock.json
}

removeGitFiles

apt-get update
apt-get upgrade

apt-get install curl
apt-get install git
apt-get install nodejs
apt-get install npm
apt-get install python3

# Install OpenVPN
echo Install OpenVPN

cd /openvpn-install

chmod +x openvpn-install.sh

./openvpn-install.sh

# Copy python scripts to OpenVPN folder
echo Copy python scripts

cd /openvpn-install

cp -R scripts /etc/openvpn/scripts

chmod -R +x /etc/openvpn/scripts

# Install OpenVPN node
echo Install OpenVPN node

cd /

git clone https://github.com/Arseniys1/openvpn-node

cd /openvpn-node

removeGitFiles

npm install

# Edit config files
echo Edit config files

nano /etc/openvpn/scripts/config.py

nano /openvpn-node/config.js

# Start OpenVPN and OpenVPN node
echo Start OpenVPN and OpenVPN node

service openvpn stop

service openvpn start

cd /openvpn-node

nohup node echo.js > /dev/null & echo $!

# Copy openvpn-install.sh to /
echo Copy openvpn-install.sh to /

cd /openvpn-install

cp openvpn-install.sh /openvpn-install.sh

# Delete openvpn-install folder
echo Delete openvpn-install folder

cd /

rm -rf openvpn-install

echo Install finish



