#!usr/bin/env python
#actualizarcausaaccionestado
# -*- coding: utf-8 -*-

import json
import logging as log
import requests
import urlservices
import selectbd
import registrarenbd

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def actualizarcausa(ipservidor, con):
    log.debug('-----Ingresando a actualizar causa-----')
    log.info('**********Metodo Actualizar Causas*******')
    rc = requests.get(urlservices.urlcausa(ipservidor))
    rcjson = rc.json()
    for value in rcjson:
        log.debug('-----Entra al for del json retornado-----')
        causas = selectbd.selectcausa(con)
        filanula = causas.fetchone()
        if filanula == None:
            log.debug('-------No existen datos en la bd--------')
            log.info('**********Se agrega la causa*******')
            registrarenbd.registrarcausa(con, str(value))
        else:
            log.debug('------Existen Causas en la base de datos------')
            for causa in causas:
                if value != str(causa[0]):
                    log.info('*****existe un valor para insertar*****')
                    valorainsertar = value
                if value == str(causa[0]):
                    valorainsertar = None
                    break
            if valorainsertar != None:
                registrarenbd.registrarcausa(con, str(valorainsertar))
    log.info('*****Fin del metodo Actualizar causa*****')

def actualizaraccion(ipservidor, con):
    log.debug('-----Ingresando a actualizar accion-----')
    log.info('**********Metodo Actualizar Accion*******')
    ra = requests.get(urlservices.urlaccion(ipservidor))
    rajson = ra.json()
    for value in rajson:
        log.debug('-----Entra al for del json retornado-----')
        acciones = selectbd.selectaccion(con)
        filanula = acciones.fetchone()
        if filanula == None:
            log.debug('-------No existen datos en la bd--------')
            log.info('**********Se agrega la accion*******')
            registrarenbd.registraraccion(con, str(value))
        else:
            log.debug('------Existen acciones en la base de datos------')
            for accion in acciones:
                if value != str(accion[0]):
                    log.info('*****existe un valor para insertar*****')
                    valorainsertar = value
                if value == str(accion[0]):
                    valorainsertar = None
                    break
            if valorainsertar != None:
                registrarenbd.registraraccion(con, str(valorainsertar))
    log.info('*****Fin del metodo Actualizar accion*****')

def actualizarestado(ipservidor, con):
    log.debug('-----Ingresando a actualizar estados-----')
    log.info('**********Metodo Actualizar Estados*******')
    re = requests.get(urlservices.urlestado(ipservidor))
    rejson = re.json()
    for value in rejson:
        log.debug('-----Entra al for del json retornado-----')
        estados = selectbd.selectestado(con)
        filanula = estados.fetchone()
        if filanula == None:
            log.debug('-------No existen datos en la bd--------')
            log.info('**********Se agrega la estado*******')
            registrarenbd.registrarestado(con, str(value))
        else:
            log.debug('------Existen Estado en la base de datos------')
            for estado in estados:
                if value != str(estado[0]):
                    log.info('*****existe un valor para insertar*****')
                    valorainsertar = value
                if value == str(estado[0]):
                    valorainsertar = None
                    break
            if valorainsertar != None:
                registrarenbd.registrarestado(con, str(valorainsertar))
    log.info('*****Fin del metodo Actualizar Estado*****')
