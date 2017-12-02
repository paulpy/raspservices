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
	lograspadmin.escribirlog("-------------------------------------------------")
	lograspadmin.escribirlog("lecturaestadoequipo")
	print "--------------------------Lectura de equipo--------------------------"
	if pingserver.isAlive(ipequipo):
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchone()
		print estados
		for estado in estados:
			print estado
			if str(estado[0])!="1":
				lograspadmin.escribirlog("Estado actual Encendido")
				registrarenbd.historicoequipo(6,1,con)
				break
			else:
				lograspadmin.escribirlog("Estado Encendido")
				break
	else:
		cursor = selectbd.selectestadoequipo(con)
		estados = cursor.fetchone()
		print estados
		for estado in estados:
			print estado
			if str(estado[0])==1:
				lograspadmin.escribirlog("Estado Apagado")
				registrarenbd.historicoequipo(6,2,con)
				break
			else:
				lograspadmin.escribirlog("Estado Apagado")
				break



"""
def lecturaestadoequipo(con):
    historico = selectbd.selectultimohee(con)
    estadoactual = historico.fetchone()
	if estadoactual[3]=="2":
		comandogpio.encender()
		registrarenbd.historicoequipo("3","6",con)
	if estadoactual[3]=="6":
		diferencia=diferenciatiempo.diferenciadehora(estadoactual[1],datetime.datetime.now)
		if diferencia > 200:
			registrarenbd.historicoequipo("3","4",con)
		else:
			pass
			"""
