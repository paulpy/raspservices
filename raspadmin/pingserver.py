#!usr/bin/env python
#pingalservidor

import os

def isAlive(ipv4, cmd_ping='ping', count=1):
	"""
	True	-	Tiene Ping con el servidor
	False	-	No tiene ping con el servidor
	"""
	if os.system('{0} -c {1} {2}'.format(cmd_ping, count, ipv4)) == 0:
		return True
	else:
		return False