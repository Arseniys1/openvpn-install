#!/usr/bin/python3
# coding=utf-8

import sys
import os
import logging
import requests
import config

user_text_id = os.environ.get("common_name")
ip = os.environ.get("trusted_ip")

data = {
	"user_text_id": user_text_id,
	"ip": ip,
}

try:
	r = requests.post(url=config.connect_url, data=data)
except Exception as e:
	logging.warning('Failed to complete server request: %s', e)
	sys.exit()
	
if r.status_code != 200:
	logging.warning('Error status server code %d and should be 200', r.status_code)
	

