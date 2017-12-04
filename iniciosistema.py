#!/usr/bin/env python
#iniciosistema

import sys
import sqlite3
import os
import datetime
import pingequipo
import escrituralog
import registrarenhistorico

escrituralog.escribirlog("Iniciando Sistema")
con = sqlite3.connect("/root/raspproyect/raspweb/db.sqlite3")
escrituralog.escribirlog("Ingreso a la Base de datos")
fechahora = datetime.datetime.now()
escrituralog.escribirlog("Inicio del SO, Agregado al historico")
registrarenhistorico.historicoraspberry(6, 4, con)
ipequipo = "192.168.0.51"
if pingequipo.isAlive(ipequipo):
	escrituralog.escribirlog("Existe Equipo, agregado al historico")
	registrarenhistorico.historicoequipo(6, 5, con)
else:
	escrituralog.escribirlog("No existe Equipo, agregado al historico")
	registrarenhistorico.historicoequipo(4, 2, con)
con.commit()
escrituralog.escribirlog("Cerrando conexion con la base de datos")
con.close()
escrituralog.escribirlog("Desplegando AppWeb Puerto 8000")
os.system("/opt/raspservices/inicioserverdjango.sh")
escrituralog.escribirlog("Culminado el proceso")
