#!usr/bin/env python
#hacercoleccion
# -*- coding: utf-8 -*-

import collections
import json
import logging as log

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def coleccion(select):
    log.info('*****Ingreso al metodo de crear coleccion******')
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
    log.info('*****Retornando coleccion fin del metodo******')
    return log_json

def coleccionraspinteraccion(select):
    log.info('******Ingreso al metodo de crear coleccion interaccion*****')
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
    log.info('*****Retornando coleccion fin del metodo*****')
    return enviodatosrasp

def coleccionenviointeraccion(select):
	log.info('*****Ingreso al mertodo crear Coleccion envio de interaccion*****')
	fechaid=[]
	for value in select:
		fechaiddatos = collections.OrderedDict()
		fechaiddatos['id'] = value[0]
		fechaiddatos['realizado'] = value[1]
		fechaid.append(fechaiddatos)
	fechahorajson = json.dumps(fechaid)
    log.info('*****Retornando coleccion Fin del metodo*****')
	return fechahorajson