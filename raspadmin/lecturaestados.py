#!/usr/bin/env python
#escaneoaequipoconectado

import datetime
import pingserver
import selectbd
import registrarenbd
import lograspadmin
import diferenciatiempo
import comandogpio

def equipoconectado(con, ipequipo):
	if pingserver.isAlive(ipequipo):
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchone()
		for estado in estados:
			if estado != 5:
				lograspadmin.escribirlog("Estado actual Encendido")
				registrarenbd.historicoequipo(6, 5, con)
				break
			else:
				lograspadmin.escribirlog("Estado Encendido")
				break
	else:
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchone()
		for estado in estados:
			if estado == 5:
				lograspadmin.escribirlog("Estado actual Apagado")
				registrarenbd.historicoequipo(6, 2, con)
				break
			else:
				lograspadmin.escribirlog("Estado Apagado")
				break

def lecturaestadoequipo(con):
	historico = selectbd.selectultimohee(con)
	estadoactual = historico.fetchall()
	for estado in estadoactual:
		print estado
		if estado[3] == 2:
			lograspadmin.escribirlog("Comprabando estado para encendido")
			comandogpio.encender()
			registrarenbd.historicoequipo(3, 4, con)
		if estado[3] == 3:
			diferencia=diferenciatiempo.diferenciadehora(estado[1], datetime.datetime.now)
			if diferencia >= 200:
				lograspadmin.escribirlog("Tiempo de reinicio muy alto estado desconectado")
				registrarenbd.historicoequipo(3, 6, con)
			else:
				pass
		break
