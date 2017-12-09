#!usr/bin/env python
#consumidorserviciosweb
# -*- coding: UTF-8 -*-

import sqlite3
import selectbd
import urlservices
import coleccion
import requests
import logging as log
import lograspadmin
import registrarenbd

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def enviarlograsp(ipservidor, con):
    log.info('*****Metodo enviar log del raspberry*****')
    select = selectbd.selectidentificadorrasp(con)
    for serie in select:
        url = urlservices.urlhistoricorasp(ipservidor, str(serie[0]))
    rc = requests.get(url)
    ultimoid = rc.json()
    if str(ultimoid) == -1:
        log.info('No Existe serie en la base de Datos Central')
    elif str(ultimoid) == 0:
        log.info('Sincronizando por Primerar Vez')
        envio = coleccion.coleccion(selectbd.selecthistoricoraspultid(ultimoid,con))
        rce = requests.post(urlservices.urlsincrohistoricorasp(ipservidor), json=envio)
    else:
        log.info('Corroborando Fila nula')
        select = selectbd.selecthistoricoraspultid(ultimoid,con)
        filanula = select.fetchall()
        if filanula != None:
            log.info('Enviando Datos para actualizar')
            envio = coleccion.coleccion(selectbd.selecthistoricoraspultid(ultimoid,con))
            rce = requests.post(urlservices.urlsincrohistoricorasp(ipservidor), json=envio)
        else:
            log.info('No es necesario sincronizar')
    log.info('*****Fin del metodo*****')

def enviarlogequi(ipservidor, con):
    log.info('*****Metodo enviar log del equipo*****')
    select = selectbd.selectidentificadorequi(con)
    for serie in select:
    	url = urlservices.urlhistoricoequi(ipservidor,str(serie[0]))
    rc = requests.get(url)
    ultimoid = rc.json()
    if str(ultimoid) == -1:
    	log.info('No Existe serie en la base de Datos Central')
    elif str(ultimoid) == 0:
    	log.info('Sincronizando por Primerar Vez')
    	envio = coleccion.coleccion(selectbd.selecthistoricoequiultid(ultimoid,con))
    	rce = requests.post(urlservices.urlsincrohistoricoequi(ipservidor), json=envio)
    else:
        log.info('Corroborando Fila nula')
        select = selectbd.selecthistoricoraspultid(ultimoid,con)
        filanula = select.fetchall()
        if filanula != None:
            log.info('Enviando Datos para actualizar')
            envio = coleccion.coleccion(selectbd.selecthistoricoequiultid(ultimoid,con))
            rce = requests.post(urlservices.urlsincrohistoricoequi(ipservidor), json=envio)
        else:
            log.info('No es necesario sincronizar')
    log.info('*****Fin del Metodo****')

def interaccionws(ipservidor, con):
    log.info('*****Metodo consumir interaccion*****')
    enviodtosrasp = coleccion.coleccionraspinteraccion(selectbd.selectraspberry(con))
    ri = requests.post(urlservices.urlinteracciones(ipservidor), json=enviodtosrasp)
    rijson = ri.json()
    for value in rijson:
        if value["idAccion"] == None:
            log.info('No trajo interacciones')
        else:
            log.info('Se encontraron interacciones')
            registrarenbd.interacciones(con,value["comando"],value["idAccion"],str(value["idInteraccion"]),str(value["codInteraccion"]))
    log.info('****Fin del Metodo*****')

def actualizarinteraccion(ipservidor, con, id):
    log.info('*****Metodo enviar actualizacion de interaccion cumplida*****')
    cursor = selectbd.selectactualizarinte(con,id)
    envioactualizar = cursor.fetchall()
    rfh = requests.post(urlservices.urlactualizarinteraccion(ipservidor), json=coleccion.coleccionenviointeraccion(envioactualizar))
    log.info('****Fin del metodo*****')
