#!/usr/bin/env python
#iniciosistema
# -*- coding: utf-8 -*-

import sqlite3
import os
import datetime
import logging as log
import pingequipo
import registrarenhistorico

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = 'loginiciosistema.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)
log.info('***********************')
log.info('Incio de InicioSistema')
log.debug('Ingrego a la base de datos')
con = sqlite3.connect("/root/raspproyect/raspweb/db.sqlite3")
fechahora = datetime.datetime.now()
log.info('Registro de Inicio del Sistema Operativo')
registrarenhistorico.historicoraspberry(6, 4, con)
ipequipo = "192.168.0.51"
if pingequipo.isAlive(ipequipo):
	log.info('Existe comunicacione con el equipo')
	log.info('Registrado com encedido')
	registrarenhistorico.historicoequipo(6, 5, con)
else:
	log.info('No existe comunicacione con el equipo')
	log.info('Registrado com apagado')
	registrarenhistorico.historicoequipo(4, 2, con)
con.commit()
con.close()
log.debug('Cerrando conexion con la Base de datos')
log.info('Iniciando Django Puerto 8000')
os.system("/opt/raspservices/inicioserverdjango.sh")
log.info('Proceso Terminando')
log.info('---------------------------------------')
