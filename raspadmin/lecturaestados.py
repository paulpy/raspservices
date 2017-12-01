#!/usr/bin/env python
#escaneoaequipoconectado

import datetime
import pingserver
import selectbd
import registrarenbd
import escrituralog
import diferenciatiempo
import comandogpio

def equipoconectado(con, ipequipo):
	if pingserver.isAlive(ipequipo):
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchall()
		for estado in estados:
			if str(estado[0])!=1:
				escrituralog.escribirlog("Estado actual Encendido")
				registrarenbd.historicoequipo(6,1,con)
				break
			else:
				escrituralog.escribirlog("Estado Encendido")
				break
	else:
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchall()
		for estado in estados:
			if str(estado[0])==1:
				escrituralog.escribirlog("Estado Apagado")
				registrarenbd.historicoequipo(6,2,con)
				break
			else:
				escrituralog.escribirlog("Estado Apagado")
				break

def lecturaestadoequipo(con):
    historico = selectbd.selectultimohee(con)
    estadoactual = historico.fetchone()
    if estadoactual[3]=="2":
        comandogpio.encender()
        registrarenbd.historicoequipo("3","6",con)
    if estadoactual[3]=="6":
        diferencia=diferenciatiempo.diferenciadehroa(estadoactual[1],datetime.datetime.now)
        if diferencia > 200:
            registrarenbd.historicoequipo("3","4",con)
        else:
            pass