#!/usr/bin/env python
#escaneoaequipoconectado

import datetime
import logging as log
import pingserver
import selectbd
import registrarenbd
import diferenciatiempo
import comandogpio

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def equipoconectado(con, ipequipo):
    log.info('***** Metodo de ping a server o equipo*****')
    if pingserver.isAlive(ipequipo):
        cursor = selectbd.selectestadoequipo(con)
        estados = cursor.fetchone()
        for estado in estados:
            if estado != 5:
                log.info('Estado actual Encendido')
                registrarenbd.historicoequipo(6, 5, con)
                break
            else:
                log.info('Estado Encendido')
                break
    else:
        cursor = selectbd.selectestadoequipo(con)
        estados = cursor.fetchone()
        for estado in estados:
            if estado == 5:
                log.info('Estado actual Apagado')
                registrarenbd.historicoequipo(6, 2, con)
                break
            else:
                log.info('Estado Apagado')
                break
    log.info('***** fin del metodo*****')

def lecturaestadoequipo(con):
    log.info('*****Metodo de lectura de estado del equipo*****')
    historico = selectbd.selectultimohee(con)
    estadoactual = historico.fetchall()
    for estado in estadoactual:
        if estado[4] == 2:
            log.info('Comprabando estado para encendido')
            comandogpio.encender()
            registrarenbd.historicoequipo(3, 4, con)
        if estado[4] == 4:
            diferencia = diferenciatiempo.diferenciadehora(estado[1])
            if diferencia >= 200:
                log.info('Tiempo de reinicio muy alto estado desconectado')
                registrarenbd.historicoequipo(3, 6, con)
            else:
                pass
        break
    log.info('******Fin del metodo ******')
