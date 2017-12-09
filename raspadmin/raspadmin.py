#!usr/bin/env python
#raspadmin

import sqlite3
import time
import logging as log
import lograspadmin
import registrarenbd
import pingserver
import consumidorserviciosweb
import lecturaestados
import cumplimientoaccion

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

con = sqlite3.connect("/root/raspproyect/raspweb/db.sqlite3")
ipservidor = "192.168.1.54"
ipequipo = "192.168.0.51"
log.info('*****----Inicio del RaspAdmin----*****')
registrarenbd.historicoraspberry(6, 1, con)
con.close()
def raspprocess():
    con = sqlite3.connect("/root/raspproyect/raspweb/db.sqlite3")
    lecturaestados.equipoconectado(con,ipequipo)
    if pingserver.isAlive(ipservidor):
        log.info('*****Existe conxion con el servidor*****')
        consumidorserviciosweb.enviarlograsp(ipservidor,con)
        consumidorserviciosweb.enviarlogequi(ipservidor,con)
        consumidorserviciosweb.interaccionws(ipservidor,con)
        cumplimientoaccion.realizarinteraccionespendientes(ipservidor,con)
    else:
        log.info('*****No existe conxion con el servidor*****')
    lecturaestados.lecturaestadoequipo(con)
    con.close()
    log.info('*****Esperando 10 Segundos*****')
    time.sleep(10)

while True:
    raspprocess()