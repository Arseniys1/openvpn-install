#!/usr/bin/python3
# coding=utf-8

import sys
import os
import time
import logging
import requests
import psutil
import config

while True:
	cpu = psutil.cpu_percent(interval=0.2)
	# ram в мб
	ram = psutil.virtual_memory()
	ram_max = "%10.3f" % (ram.total / 2**10)
	ram_used = "%10.3f" % (ram.used / 2**10)
	# hdd в гб
	hdd = psutil.disk_usage('/')
	hdd_max = "%10.3f" % (hdd.total / 2**20)
	hdd_used = "%10.3f" % (hdd.used / 2**20)
	
	data = {
		"cpu": cpu,
		"ram_max": ram_max,
		"ram": ram_used,
		"hdd_max": hdd_max,
		"hdd": hdd_used,
	}
	
	try:
		r = requests.post(url=config.stat_url, data=data)
		
		if r.status_code != 200:
			logging.warning('Error status server code %d and should be 200', r.status_code)
	except Exception as e:
		logging.warning('Failed to complete server request: %s', e)
	
	time.sleep(900) # 15 минут



