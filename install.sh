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

# Install OpenVPN node
echo Install OpenVPN node

cd /

git clone https://github.com/Arseniys1/openvpn-node

cd /openvpn-node

removeGitFiles

echo Install finish



