#!usr/bin/env python
#hacercoleccion

import collections
import json

def coleccion(select):
	log_db = select.fetchall()
	lista_log = []
	for log in log_db:
		t_log = collections.OrderedDict()
		t_log['id'] = log[0]
		t_log['momento'] = log[1]
		t_log['causa'] = log[2]
		t_log['estado'] = log[3]
		t_log['equipo'] = log[4]
		lista_log.append(t_log)
	log_json = json.dumps(lista_log)
	return log_json

def coleccionraspinteraccion(select):
	datosrasp = select.fetchall()
	raspdatosjson = []
	for rasp in datosrasp:
		raspdato = collections.OrderedDict()
		raspdato['id'] = rasp[0]
		raspdato['ip'] = rasp[1]
		raspdato['raspIdentificador'] = rasp[2]
		raspdato['equipo'] = rasp[3]
		raspdatosjson.append(raspdato)
	enviodatosrasp = json.dumps(raspdatosjson)
	return enviodatosrasp

def coleccionenviointeraccion(select):
	#datosinteraccion = select.fetchall()
	fechaid=[]
	for value in select:
		fechaiddatos = collections.OrderedDict()
		fechaiddatos['id'] = value[0]
		fechaiddatos['realizado'] = value[1]
		fechaid.append(fechaiddatos)
	fechahorajson = json.dumps(fechaid)
	return fechahorajson