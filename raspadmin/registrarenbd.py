#!/usr/bin/env python
#registrarenbd

import datetime
import lograspadmin

def historicoraspberry(causa, estado, con):
	lograspadmin.escribirlog("Insercion en historicoraspberry")
	fechahora=datetime.datetime.now()
	cursor = con.cursor()
	cursor.execute("INSERT INTO raspapp_historico_estado_raspberry (fecha_hora_equipo_raspberry, causa_raspberry_fk_id, estado_raspberry_fk_id, raspberry_asignado_fk_id) VALUES (\'"+str(fechahora)+"\' ,"+str(causa)+","+str(estado)+",1)")
	con.commit()

def historicoequipo(causa, estado, con):
	lograspadmin.escribirlog("Insercion en historicoequipo")
	fechahora = datetime.datetime.now()
	cursor = con.cursor()
	cursor.execute("INSERT INTO raspapp_historico_estado_equipo (fecha_hora_equipo_estado, causa_equipo_fk_id, estado_equipo_fk_id, equipo_asignado_fk_id) VALUES (\'"+str(fechahora)+"\' ,"+str(causa)+","+str(estado)+",1)")
	con.commit()

def interacciones(con, comando, idAccion, idInteraccion, codInteraccion):
	lograspadmin.escribirlog("Insercion en Interacciones")
	fechahora = datetime.datetime.now()
	cursor = con.cursor()
	cursor.execute("INSERT INTO raspapp_interaccion (interaccion_fecha_hora_re, interaccion_comando, interaccion_accion_fk_id, interaccion_equipo_fk_id, interaccion_raspberry_fk_id, interaccion_id_interaccion, interaccion_codigo, interaccion_activo) VALUES (\'"+str(fechahora)+"\',\'"+str(comando)+"\',"+str(idAccion)+",1,1,"+str(idInteraccion)+","+str(codInteraccion)+",0)")
	con.commit()

def registraraccion(con, accion):
	lograspadmin.escribirlog("Insercion en Accion")
	cursor = con.cursor()
	cursor.execute("INSERT INTO raspapp_accion (accion) VALUES (?);", [accion])
	con.commit()

def registrarestado(con, estado):
	lograspadmin.escribirlog("Insercion en Accion")
	cursor = con.cursor()
	cursor.execute("INSERT INTO raspapp_estados_equipos (estado_equipo) VALUES (?);", [estado])
	con.commit()

def registrarcausa(con, causa):
	lograspadmin.escribirlog("Insercion en Accion")
	cursor = con.cursor()
	cursor.execute("INSERT INTO raspapp_causas_cambios (causa_cambio) VALUES (?);", [causa])
	con.commit()

def actualizarinteraccionbdlocal(con, interaccion):
	lograspadmin.escribirlog("Actualizacion de Interaccion")
	fechahora = datetime.datetime.now()
	cursor = con.cursor()
	cursor.execute("UPDATE raspapp_interaccion SET interaccion_fecha_hora_re = \'"+str(fechahora)+"\' , interaccion_activo = 1 WHERE id = "+str(interaccion))
	con.commit()
