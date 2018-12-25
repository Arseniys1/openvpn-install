#!/usr/bin/python3
# coding=utf-8

import sys
import os
import logging
import requests
import config

if config.show_time:
	import time
	
	start_time = time.perf_counter()
	

SUCCESS_AUTH = 0
ERROR_AUTH = 1

username = os.environ.get("username")
password = os.environ.get("password")
ip = os.environ.get("untrusted_ip")
port = os.environ.get("untrusted_port")

logging.info('Authorization attempt for username: %s ip: %s port: %s', username, ip, port)

data = {
	"username": username,
	"password": password,
	"ip": ip,
	"port": port,
}

try:
	r = requests.post(url=config.verify_url, data=data)
except Exception as e:
	logging.warning('Failed to complete server request: %s', e)
	sys.exit(ERROR_AUTH)


if r.status_code != 200:
	logging.warning('Error status server code %d and should be 200', r.status_code)
	sys.exit(ERROR_AUTH)
	
	
if config.show_time:
	stop_time = time.perf_counter()
	diff_time = str(config.toFixed((stop_time - start_time), 2))
	logging.info('Request time: %d seconds', diff_time)
	

try:
	r_json = r.json()
except Exception:
	logging.warning('Server error returned not json')
	sys.exit(ERROR_AUTH)


if r_json["ok"] == False:
	logging.warning('Authorisation Error. Server message: %s', r_json["message"])
	sys.exit(ERROR_AUTH)
else:
	logging.info('Successful authorization username: %s ip: %s port: %s', username, ip, port)
	sys.exit(SUCCESS_AUTH)
	