#!usr/bin/env python
#consumidorserviciosweb

import sqlite3
import selectbd
import urlservices
import lograspadmin
import coleccion
import requests
import registrarenbd

def enviarlograsp(ipservidor, con):
	lograspadmin.escribirlog("Verificando Sincronizacion del Raspberry")
	select = selectbd.selectidentificadorrasp(con)
	for serie in select:
		url = urlservices.urlhistoricorasp(ipservidor, str(serie[0]))
	rc = requests.get(url)
	ultimoid = rc.json()
	if str(ultimoid) == -1:
		lograspadmin.escribirlog("No Existe serie en la base de Datos Central")
	elif str(ultimoid) == 0:
		lograspadmin.escribirlog("Sincronizando por Primerar Vez")
		envio = coleccion.coleccion(selectbd.selecthistoricoraspultid(ultimoid,con))
		rce = requests.post(urlservices.urlsincrohistoricorasp(ipservidor), json=envio)
	else:
		lograspadmin.escribirlog("Corroborando Fila nula")
		select = selectbd.selecthistoricoraspultid(ultimoid,con)
		filanula = select.fetchall()
		if filanula != None:
			lograspadmin.escribirlog("Enviando Datos para actualizar")
			envio = coleccion.coleccion(selectbd.selecthistoricoraspultid(ultimoid,con))
			rce = requests.post(urlservices.urlsincrohistoricorasp(ipservidor), json=envio)
		else:
			lograspadmin.escribirlog("No es necesario sincronizar")

def enviarlogequi(ipservidor, con):
	lograspadmin.escribirlog("Verificando Sincronizacion del Equipo")
	select = selectbd.selectidentificadorequi(con)
	for serie in select:
		url = urlservices.urlhistoricoequi(ipservidor,str(serie[0]))
	rc = requests.get(url)
	ultimoid = rc.json()
	if str(ultimoid) == -1:
		lograspadmin.escribirlog("No Existe serie en la base de Datos Central")
	elif str(ultimoid) == 0:
		lograspadmin.escribirlog("Sincronizando por Primerar Vez")
		envio = coleccion.coleccion(selectbd.selecthistoricoequiultid(ultimoid,con))
		rce = requests.post(urlservices.urlsincrohistoricoequi(ipservidor), json=envio)
	else:
		lograspadmin.escribirlog("Corroborando Fila nula")
		select = selectbd.selecthistoricoraspultid(ultimoid,con)
		filanula = select.fetchall()
		if filanula != None:
			lograspadmin.escribirlog("Enviando Datos para actualizar")
			envio = coleccion.coleccion(selectbd.selecthistoricoequiultid(ultimoid,con))
			rce = requests.post(urlservices.urlsincrohistoricoequi(ipservidor), json=envio)
		else:
			lograspadmin.escribirlog("No es necesario sincronizar")

def interaccionws(ipservidor,con):
	lograspadmin.escribirlog("Consumiendo Servicio Web de Interaccion")
	enviodtosrasp = coleccion.coleccionraspinteraccion(selectbd.selectraspberry(con))
	ri = requests.post(urlservices.urlinteracciones(ipservidor), json=enviodtosrasp)
	rijson = ri.json()
	for value in rijson:
		if value["idAccion"] == None:
			lograspadmin.escribirlog("No trajo interacciones")
		else:
			lograspadmin.escribirlog("Se encontraron interacciones")
			registrarenbd.interacciones(con,value["comando"],value["idAccion"],str(value["idInteraccion"]),str(value["codInteraccion"]))

def actualizarinteraccion(ipservidor,con,id):
	lograspadmin.escribirlog("Consumiendo Servicio Web de Actualizar Interaccion")
	cursor = selectbd.selectactualizarinte(con,id)
	envioactualizar = cursor.fetchall()
	rfh = requests.post(urlservices.urlactualizarinteraccion(ipservidor), json=coleccion.coleccionenviointeraccion(envioactualizar))