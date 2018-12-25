#!/usr/bin/python3
# coding=utf-8

import sys
import os
import logging
import requests
import config

username = os.environ.get("username")
ip = os.environ.get("untrusted_ip")
port = os.environ.get("untrusted_port")

data = {
	"username": username,
	"ip": ip,
	"port": port,
}

try:
	r = requests.post(url=config.connect_url, data=data)
except Exception as e:
	logging.warning('Failed to complete server request: %s', e)
	sys.exit()
	
if r.status_code != 200:
	logging.warning('Error status server code %d and should be 200', r.status_code)
	

