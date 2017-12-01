#!usr/bin/env python
#registrarhistorico

import sqlite3
import escrituralog
import datetime

def historicoraspberry(causa,estado,con):
	cursor = con.cursor()
	escrituralog.escribirlog("Insercion en historicoraspberry")
	fechahora=datetime.datetime.now()
	cursor.execute("INSERT INTO raspapp_historico_estado_raspberry (fecha_hora_equipo_raspberry, causa_raspberry_fk_id, estado_raspberry_fk_id, raspberry_asignado_fk_id) VALUES (\'"+str(fechahora)+"\' ,"+str(causa)+","+str(estado)+",1)")
	con.commit()

def historicoequipo(causa,estado,con):
	cursor = con.cursor()
	escrituralog.escribirlog("Insercion en historicoequipo")
	fechahora=datetime.datetime.now()
	cursor.execute("INSERT INTO raspapp_historico_estado_equipo (fecha_hora_equipo_estado, causa_equipo_fk_id, estado_equipo_fk_id, equipo_asignado_fk_id) VALUES (\'"+str(fechahora)+"\' ,"+str(causa)+","+str(estado)+",1)")
	con.commit()

			