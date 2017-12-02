#!usr/bin/env python
#seleccionarinteraccion

import lograspadmin
import actualizarcae
import consumidorserviciosweb
import comandosparaejecutar
import conectarequipo
import comandogpio
import registrarenbd

def sincronizaraccion(ipservidor, con, idinteraccion):
	lograspadmin.escribirlog("Sincronizando Acciones")
	actualizarcae.actualizaraccion(ipservidor, con)
	registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)

def sincronizarestado(ipservidor, con, idinteraccion):
	lograspadmin.escribirlog("Sincronizando Estados")
	actualizarcae.actualizarestado(ipservidor, con)
	registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)

def sincronizarcausa(ipservidor, con, idinteraccion):
	lograspadmin.escribirlog("Sincronizando Causas")
	actualizarcae.actualizarcausa(ipservidor, con)
	registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)

def apagarraspberry(ipservidor, con, idinteraccion):
	lograspadmin.escribirlog("Apagando Raspberry")
	registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
	registrarenbd.historicoraspberry(6,1,con)
	comandosparaejecutar.apagarrasp()

def reiniciarraspberry(ipservidor, con, idinteraccion):
	lograspadmin.escribirlog("Reiniciar Raspberry")
	registrarenbd.actualizarinteraccionbdlocal(con, idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor, con, idinteraccion)
	registrarenbd.historicoraspberry(6,6,con)
	comandosparaejecutar.reiniciarrasp()

def cambiarfhora(ipservidor, con, interaccion):
	lograspadmin.escribirlog("Cambiar Fecha-Hora")
	registrarenbd.actualizarinteraccionbdlocal(con, str(interaccion[4]))	
	consumidorserviciosweb.actualizarinteraccion(ipservidor, con, str(interaccion[4]))
	registrarenbd.historicoraspberry(6,6,con)
	fechaohora = interaccion[2]
	lograspadmin.escribirlog(fechaohora)
	comando="date --set \'"+str(fechaohora[0:15])+"\'"
	comandosparaejecutar.ejecutarcomandosgenerico(comando)

def sinchorario(ipservidor,con,interaccion):
	lograspadmin.escribirlog("Cambiar Fecha hora en Equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,str(interaccion[4]))
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,str(interaccion[4]))
	registrarenbd.historicoequipo(6,6,con)
	fechahora = interaccion[2]
	comando="date --set \'"+str(fechahora[0:15])+"\'"
	comandosparaejecutar.cambiarfechahora(comando)

def apagarequipo(ipservidor, con, idinteraccion):
	lograspadmin.escribirlog("Apagando Equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,1,con)
	conectarequipo.cumplicomando("shutdown")

def reiniciarequipo(ipservidor,con,idinteraccion):
	lograspadmin.escribirlog("Apagando Equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,6,con)
	conectarequipo.cumplicomando("reboot")

def encenderequipo(ipservidor,con,idinteraccion):
	lograspadmin.escribirlog("Encender Equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,6,con)
	comandogpio.encender()

def iniciarsubsistem(ipservidor,con,idinteraccion):
	lograspadmin.escribirlog("Iniciar SubSistema del equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,6,con)
	conectarequipo.cumplicomando("/etc/rc.cism start")

def pararsubsistem(ipservidor,con,idinteraccion):
	lograspadmin.escribirlog("Parar SubSistema del equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,6,con)
	conectarequipo.cumplicomando("/etc/rc.cism stop")

def reiniciarsubsistem(ipservidor,con,idinteraccion):
	lograspadmin.escribirlog("Reiniciar SubSistema del equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,6,con)
	conectarequipo.cumplicomando("/etc/rc.cism restart")

def crearbackupespacio(ipservidor,con,idinteraccion):
	lograspadmin.escribirlog("Crear backup de bd del equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,6,con)
	conectarequipo.cumplicomando("mysqldump -u root -pwinner cism > cism.sql")

def enviarcomando(ipservidor, con, idinteraccion, comando):
	lograspadmin.escribirlog("ejecutarcomando en el equipo")
	registrarenbd.actualizarinteraccionbdlocal(con,idinteraccion)
	consumidorserviciosweb.actualizarinteraccion(ipservidor,con,idinteraccion)
	registrarenbd.historicoequipo(6,6,con)
	conectarequipo.cumplicomando(comando)