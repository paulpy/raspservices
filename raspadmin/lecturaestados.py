#!/usr/bin/env python
#escaneoaequipoconectado

import pingserver
import selectbd
import registrarenbd

def equipoconectado(con,ipequipo):
	if pingserver.isAlive(ipequipo):
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchall()
		for estado in estados:
			if (str(estado[0])!=1):
				escrituralog.escribirlog("Estado Encendido")
				registrarembd.historicoequipo(6,1,con)
				break
			else:
				escrituralog.escribirlog("Estado Encendido")
				break
	else:
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchall()
		for estado in estados:
			if (str(estado[0])==1):
				escrituralog.escribirlog("Estado Apagado")
				registrarembd.historicoequipo(6,2,con)
				break
			else:
				escrituralog.escribirlog("Estado Apagado")
				break