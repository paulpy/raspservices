import os

def isAlive(ipv4, cmd_ping='ping', count=1):
	"""
	True	-	Tiene Ping con el equipo
	False	-	No tiene ping con el equipo
	"""
	if os.system('{0} -c {1} {2}'.format(cmd_ping, count, ipv4)) == 0:
		return True
	else:
		return False