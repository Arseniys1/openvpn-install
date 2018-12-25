url = "https://cp.siberia-vpn.com/api/vpn/{0}"
token = "bo3Jg6peTyUYHmiIXFsgVdTQk0Pcb5"
url = url.format(token)
verify_url = url + "/verify"
connect_url = url + "/connect"
disconnect_url = url + "/disconnect"
stat_url = url + "/stat"

show_time = True

def toFixed(numObj, digits=0):
	return f"{numObj:.{digits}f}"

