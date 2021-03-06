#!usr/bin/env python
#seleccionarinteraccion

import logging as log
import lograspadmin
import actualizarcae
import consumidorserviciosweb
import comandosparaejecutar
import conectarequipo
import comandogpio
import registrarenbd

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def sincronizaraccion(ipservidor, con, idinteraccion):
    log.info('Sincronizando Acciones')
    actualizarcae.actualizaraccion(ipservidor, con)
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)

def sincronizarestado(ipservidor, con, idinteraccion):
    log.info('Sincronizando Estados')
    actualizarcae.actualizarestado(ipservidor, con)
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)

def sincronizarcausa(ipservidor, con, idinteraccion):
    log.info('Sincronizando Causas')
    actualizarcae.actualizarcausa(ipservidor, con)
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)

def apagarraspberry(ipservidor, con, idinteraccion):
    log.info('Apagando Raspberry')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    registrarenbd.historicoraspberry(5, 2, con)
    comandosparaejecutar.apagarrasp()

def reiniciarraspberry(ipservidor, con, idinteraccion):
    log.info('Reiniciar Raspberry')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    registrarenbd.historicoraspberry(5, 3, con)
    comandosparaejecutar.reiniciarrasp()

def cambiarfhora(ipservidor, con, interaccion):
    log.info('Cambiar Fecha-Hora')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, str(interaccion[4]), codigoestado)	
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, str(interaccion[4]))
    fechaohora = interaccion[0]
    comando="date --set=\'"+str(fechaohora[0:16])+"\'"
    comandosparaejecutar.ejecutarcomandosgenerico(comando)

def sinchorario(ipservidor, con, interaccion):
    log.info('Cambiar Fecha hora en Equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, str(interaccion[4]), codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, str(interaccion[4]))
    fechahora = interaccion[0]
    comando="date --set=\'"+str(fechahora[0:16])+"\'"
    conectarequipo.cumplicomando(comando)

def apagarequipo(ipservidor, con, idinteraccion):
    log.info('Apagando Equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    registrarenbd.historicoequipo(5, 2, con)
    conectarequipo.cumplicomando("shutdown")

def reiniciarequipo(ipservidor, con, idinteraccion):
    log.info('Reiniciando Equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    registrarenbd.historicoequipo(5, 3, con)
    conectarequipo.cumplicomando("reboot")

def encenderequipo(ipservidor, con, idinteraccion, codigoestado):
    log.info('Encender Equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    registrarenbd.historicoequipo(5, 5, con)
    comandogpio.encender()

def iniciarsubsistem(ipservidor, con, idinteraccion):
    log.info('Iniciar SubSistema del equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    conectarequipo.cumplicomando("/etc/rc.cism start")

def pararsubsistem(ipservidor, con, idinteraccion):
    log.info('Parar SubSistema del equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    conectarequipo.cumplicomando("/etc/rc.cism stop")

def reiniciarsubsistem(ipservidor, con, idinteraccion):
    log.info('Reiniciar SubSistema del equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    conectarequipo.cumplicomando("/etc/rc.cism restart")

def crearbackupespacio(ipservidor, con, idinteraccion):
    log.info('Crear backup de bd del equipo')
    codigoestado = 0
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
    conectarequipo.cumplicomando("mysqldump -u root -pwinner cism > cism.sql")

def enviarcomando(ipservidor, con, idinteraccion, comando):
    log.info('ejecutarcomando en el equipo')
    codigoestado = conectarequipo.cumplicomando(comando)
    registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion, codigoestado)
    consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
