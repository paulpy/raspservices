#!/usr/bin/env python
#iniciosistema
# -*- coding: utf-8 -*-

import os
import logging as log

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = 'loginiciosistema.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def isAlive(ipv4, cmd_ping='ping', count=1):
	"""
	True	-	Tiene Ping con el equipo
	False	-	No tiene ping con el equipo
	"""
	log.info('Consultando Ping con el equipo')
	if os.system('{0} -c {1} {2}'.format(cmd_ping, count, ipv4)) == 0:
		log.info('Existe ping con el equipo')
		return True
	else:
		log.info('No existe ping con el equipo')
		return False
	log.info('Finalizando Metodo')
	log.info('-------------------------------')