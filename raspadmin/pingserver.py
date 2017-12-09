#!usr/bin/env python
#pingalservidor

import os
import logging as log

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def isAlive(ipv4, cmd_ping='ping', count=1):
    """
	True	-	Tiene Ping con el servidor
	False	-	No tiene ping con el servidor
	"""
    log.info('*****Metodo de lectura de ping*****')
    if os.system('{0} -c {1} {2}'.format(cmd_ping, count, ipv4)) == 0:
        log.info('Existe ping con el equipo o servidor')
        return True
    else:
        log.info('No existe ping con el equipo o servidor')
        return False
    log.info('*****Fin del metodo*****')
    