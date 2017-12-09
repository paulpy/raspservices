#!usr/bin/env python
#cumplimientoaccion
# -*- coding: UTF-8 -*-

import sqlite3
import logging as log
import selectbd
import lograspadmin
import actualizarcae
import seleccionarinteraccion
import consumidorserviciosweb

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def filtrointeraccion(ipservidor, con, interaccion):
    if interaccion[1] == 70:
        log.info('Sincronizar Acciones en el Raspberry')
        seleccionarinteraccion.sincronizaraccion(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 50:
        log.info('Sinconizar Estados en el Raspberry')
        seleccionarinteraccion.sincronizarestado(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 80:
        log.info('Sinconizar Causas en el Raspberry')
        seleccionarinteraccion.sincronizarcausa(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 20:
        log.info('Reiniciar el Raspberry')
        seleccionarinteraccion.reiniciarraspberry(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 10:
        log.info('Apagar el Raspberry')
        seleccionarinteraccion.apagarraspberry(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 40:
        log.info('Actualizando hora')
        lograspadmin.escribirlog(str(interaccion))
        seleccionarinteraccion.cambiarfhora(ipservidor, con, interaccion)
    if interaccion[1] == 11:
        log.info('Apagar Equipo')
        seleccionarinteraccion.apagarequipo(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 21:
        log.info('Reinicio Equipo')
        seleccionarinteraccion.reiniciarequipo(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 31:
        log.info('Encendido Equipo')
        seleccionarinteraccion.encenderequipo(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 41:
        log.info('Sincronizar Fechahora Equipo')
        seleccionarinteraccion.sinchorario(ipservidor, con, interaccion)
    if interaccion[1] == 61:
        log.info('Crear backup de SubSistema Equipo')
        seleccionarinteraccion.crearbackupespacio(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 91:
        log.info('Ejecutar inicio SubSistema Equipo')
        seleccionarinteraccion.iniciarsubsistem(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 101:
        log.info('Ejecutar reinicio SubSistema Equipo')
        seleccionarinteraccion.reiniciarsubsistem(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 111:
        log.info('Ejecutar Stop SubSistema Equipo')
        seleccionarinteraccion.pararsubsistem(ipservidor, con, str(interaccion[4]))
    if interaccion[1] == 121:
        log.info('Ejecutar Comando enviado')
        seleccionarinteraccion.enviarcomando(ipservidor, con, str(interaccion[4]), str(interaccion[2]))
def realizarinteraccionespendientes(ipservidor, con):
    log.info('****Ingresando ametodo de seleccion de interaccion******')
    select = selectbd.selectinteraccionpendiente(con)
    interacciones = select.fetchall()
    for interaccion in interacciones:
        filtrointeraccion(ipservidor, con, interaccion)
    log.info('*****Fin del metodo*****')
