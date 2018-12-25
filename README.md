# openvpn-install
OpenVpn scripts

chmod +x openvpn-install.sh
./openvpn-install.sh

cd scripts
chmod -R +x

#OpenVpn config

auth-user-pass-verify /etc/openvpn/verify.py via-env
client-connect /etc/openvpn/connect.py
client-disconnect /etc/openvpn/disconnect.py

script-security 3
