#!usr/bin/env python
#actualizarcausaaccionestado

import requests
import urlservices
import json
import sqlite3
import selectbd
import registrarenbd
import escribirenlog

def actualizarcausa(ipservidor,con):
	rc = requests.get(urlservices.urlcausa(ipservidor))
	rcjson = rc.json()
	for value in rcjson:
		causas = selectbd.selectcausa(con)
		filanula = causas.fetchall()
		if filanula == None:
			registrarenbd.registrarcausa(con,str(value))
			lograspadmin.escribirlog("Se agrega causa "+str(value))
		else:
			for causa in causas:
				if value != str(causa[0]):
					valorainsertar = value
				if value == str(causa[0]):
					valorainsertar = None
					break
			if valorainsertar != None
				registrarenbd.registrarcausa(con,str(valorainsertar))
				lograspadmin.escribirlog("Se agrega causa "+str(value))

def actualizaraccion(ipservidor,con):
	ra = requests.get(urlservices.urlaccion(ipservidor))
	rajson = ra.json()
	for value in rajson:
		acciones = selectbd.selectaccion(con)
		filanula = acciones.fetchall()
		if filanula == None:
			registrarenbd.registraraccion(con,str(value))
			lograspadmin.escribirlog("Se agrega accion "+str(value))
		else:
			for accion in acciones:
				if value != str(accion[0]):
					valorainsertar = value
				if value == str(accion[0]):
					valorainsertar = None
					break
			if valorainsertar != None
				registrarenbd.registraraccion(con,str(valorainsertar))
				lograspadmin.escribirlog("Se agrega accion "+str(value))

def actualizarestado(ipservidor,con):
	re = requests.get(urlservices.urlestado(ipservidor))
	rejson = re.json()
	for value in rejson:
		estados = selectbd.selectestado(con)
		filanula = estados.fetchall()
		if filanula == None:
			registrarenbd.registrarestado(con,str(value))
			lograspadmin.escribirlog("Se agrega estado "+str(value))
		else:
			for estado in estados:
				if value != str(estado[0]):
					valorainsertar = value
				if value == str(estado[0]):
					valorainsertar = None
					break
			if valorainsertar != None
				registrarenbd.registrarestado(con,str(valorainsertar))
				lograspadmin.escribirlog("Se agrega estado "+str(value))
