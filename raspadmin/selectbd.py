#!usr/bin/env python
#selecciondetodoslosdatosdelabd

import sqlite3

def selectidentificadorrasp(con):
	cursor = con.cursor()
	cursor.execute("SELECT identificador_raspberry FROM raspapp_raspberrys")
	return cursor

def selectidentificadorequi(con):
	cursor = con.cursor()
	cursor.execute("SELECT identificador_equipo FROM raspapp_equipo")
	return cursor

def selecthistoricoraspultid(id,con):
	cursor = con.cursor()
	cursor.execute("SELECT raspapp_historico_estado_raspberry.id, raspapp_historico_estado_raspberry.fecha_hora_equipo_raspberry, raspapp_causas_cambios.causa_cambio, raspapp_estados_equipos.estado_equipo, raspapp_raspberrys.identificador_raspberry FROM raspapp_historico_estado_raspberry, raspapp_causas_cambios, raspapp_raspberrys, raspapp_estados_equipos WHERE raspapp_historico_estado_raspberry.causa_raspberry_fk_id=raspapp_causas_cambios.id AND raspapp_historico_estado_raspberry.raspberry_asignado_fk_id=raspapp_raspberrys.id AND raspapp_historico_estado_raspberry.estado_raspberry_fk_id=raspapp_estados_equipos.id AND raspapp_historico_estado_raspberry.id > "+str(id))
	return cursor

def selecthistoricoequiultid(id,con):
	cursor = con.cursor()
	cursor.execute("SELECT raspapp_historico_estado_equipo.id, raspapp_historico_estado_equipo.fecha_hora_equipo_estado, raspapp_causas_cambios.causa_cambio, raspapp_estados_equipos.estado_equipo, raspapp_equipo.identificador_equipo FROM raspapp_historico_estado_equipo, raspapp_causas_cambios, raspapp_equipo, raspapp_estados_equipos WHERE raspapp_historico_estado_equipo.causa_equipo_fk_id=raspapp_causas_cambios.id AND raspapp_historico_estado_equipo.equipo_asignado_fk_id=raspapp_equipo.id AND raspapp_historico_estado_equipo.estado_equipo_fk_id=raspapp_estados_equipos.id AND raspapp_historico_estado_equipo.id > "+str(id))
	return cursor

def selectraspberry(con):
	cursor = con.cursor()
	cursor.execute("SELECT * FROM raspapp_raspberrys")
	return cursor

def selectinteraccionpendiente(con):
	cursor = con.cursor()
	cursor.execute("SELECT raspapp_interaccion.interaccion_comando, raspapp_interaccion.interaccion_codigo, raspapp_interaccion.interaccion_accion_fk_id, raspapp_interaccion.interaccion_id_interaccion, raspapp_interaccion.id FROM raspapp_interaccion WHERE raspapp_interaccion.interaccion_activo = 0 ORDER BY raspapp_interaccion.id ASC")
	return cursor

def selectaccion(con):
	cursor = con.cursor()
	cursor.execute("SELECT accion FROM raspapp_accion")
	return cursor

def selectestado(con):
	cursor = con.cursor()
	cursor.execute("SELECT estado_equipo FROM raspapp_estados_equipos")
	return cursor

def selectcausa(con):
	cursor = con.cursor()
	cursor.execute("SELECT causa_cambio FROM raspapp_causas_cambios")
	return cursor

def selectactualizarinte(con,id):
	cursor = con.cursor()
	cursor.execute("SELECT interaccion_id_interaccion, interaccion_fecha_hora_re FROM raspapp_interaccion where id = "+id+";")
	return cursor

def selectestadoequipo(con):
	cursor = con.cursor()
	cursor.execute("SELECT estado_equipo_fk_id FROM raspapp_historico_estado_equipo ORDER BY id DESC")
	return cursor

def selectultimohee(con):
	cursor = con.cursor()
	cursor.execute("SELECT * FROM raspapp_historico_estado_equipo ORDER BY id DESC")
	return cursor