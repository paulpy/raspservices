#!/usr/bin/env python
#iniciosistema
# -*- coding: utf-8 -*-

import sqlite3
import os
import datetime
import logging
import pingequipo
import registrarenhistorico

logging.basicConfig(filename='testlog.log', lavel=logging.INFO,
					format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("--------------------------------------------------------------------")
logging.info("Iniciando Sistema")
#con = sqlite3.connect("/root/raspproyect/raspweb/db.sqlite3")
logging.info("Ingreso a la Base de datos")
#fechahora = datetime.datetime.now()
logging.info("Inicio del SO, Agregado al historico")
#registrarenhistorico.historicoraspberry(6, 4, con)
#ipequipo = "192.168.0.51"
#if pingequipo.isAlive(ipequipo):
#	logging.info("Existe Equipo, agregado al historico")
#	registrarenhistorico.historicoequipo(6, 5, con)
#else:
#	logging.info("No existe Equipo, agregado al historico")
#	registrarenhistorico.historicoequipo(4, 2, con)
#con.commit()
logging.info("Cerrando conexion con la base de datos")
#con.close()
logging.info("Desplegando AppWeb Puerto 8000")
#os.system("/opt/raspservices/inicioserverdjango.sh")
logging.info("Culminado el proceso")
