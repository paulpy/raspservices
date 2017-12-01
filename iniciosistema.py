#!/usr/bin/env python
#iniciosistema

import sys
import sqlite3
import datetime
import pingequipo
import os
import datetime
import escrituralog
import registrarenhistorico

import logging

LOG_FORMAT = ('%(asctime)s - %(levelname)s - %(name)-40s : %(message)s')
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT)
LOGGER = logging.getLogger(__name__)


escrituralog.escribirlog("Iniciando Sistema")
LOGGER.info('Iniciando sistema...')
con = sqlite3.connect("/root/raspadmin/raspweb/db.sqlite3")
escrituralog.escribirlog("Ingreso a la Base de datos")
fechahora=datetime.datetime.now()
escrituralog.escribirlog("Inicio del SO, Agregado al historico")
registrarenhistorico.historicoraspberry("6","1",con)
ipequipo = "192.168.0.51"
if pingequipo.isAlive(ipequipo):
	escrituralog.escribirlog("Existe Equipo, agregado al historico")
	registrarenhistorico.historicoequipo("6","1",con)
else:
	escrituralog.escribirlog("No existe Equipo, agregado al historico")
	registrarenhistorico.historicoequipo("6","1",con)
con.commit()
escrituralog.escribirlog("Cerrando conexion con la base de datos")
con.close()
escrituralog.escribirlog("Desplegando AppWeb Puerto 8000")
os.system("/opt/raspservice/inicioserverdjango.sh")
escrituralog.escribirlog("Culminado el proceso")
