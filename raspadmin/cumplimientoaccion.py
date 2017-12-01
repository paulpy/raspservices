#!usr/bin/env python
#cumplimientoaccion

import sqlite3
import selectbd
import lograspadmin
import actualizarcae
import seleccionarinteraccion
import consumidorserviciosweb

def filtrointeraccion(ipservidor, con, interaccion):
	if interaccion[1]==70:
		lograspadmin.escribirlog("Sincronizar Acciones en el Raspberry")
		seleccionarinteraccion.sincronizaraccion(ipservidor,con,str(interaccion[4]))
	if(interaccion[1]==50):
		lograspadmin.escribirlog("Sinconizar Estados en el Raspberry")
		seleccionarinteraccion.sincronizarestado(ipservidor,con,str(interaccion[4]))
	if(interaccion[1]==80):
		lograspadmin.escribirlog("Sinconizar Causas en el Raspberry")
		seleccionarinteraccion.sincronizarcausa(ipservidor,con,str(interaccion[4]))
	if(interaccion[1]==20):
		lograspadmin.escribirlog("Reiniciar el Raspberry")
		seleccionarinteraccion.reiniciarraspberry(ipservidor,con,str(interaccion[4]))
	if(interaccion[1]==10):
		lograspadmin.escribirlog("Apagar el Raspberry")
		seleccionarinteraccion.apagarraspberry(ipservidor,con,str(interaccion[4]))
	if(interaccion[1]==40):
		lograspadmin.escribirlog("Actualizando hora")
		fechahoraactual = interaccion[0]
		seleccionarinteraccion.cambiarfhora(ipservidor,con,fechahoraactual)
	if(interaccion[1]==11):
		lograspadmin.escribirlog("Apagar Equipo")
		
	if(interaccion[1]==21):
		lograspadmin.escribirlog("Reinicio Equipo")

	if(interaccion[1]==31):
		lograspadmin.escribirlog("Encendido Equipo")

	if(interaccion[1]==41):
		lograspadmin.escribirlog("Sincronizar Fechahora Equipo")
		fechahoraactual = interaccion[0]
		seleccionarinteraccion.sinchorario(ipservidor,con,fechahoraactual)
		
	if(interaccion[1]==61):
		lograspadmin.escribirlog("Crear backup de SubSistema Equipo")
		
	if(interaccion[1]==91):
		lograspadmin.escribirlog("Ejecutar inicio SubSistema Equipo")

	if(interaccion[1]==101):
		lograspadmin.escribirlog("Ejecutar reinicio SubSistema Equipo")

	if(interaccion[1]==111):
		lograspadmin.escribirlog("Ejecutar Stop SubSistema Equipo")

	if(interaccion[1]==121):
		lograspadmin.escribirlog("Ejecutar Comando enviado")
		

def realizarinteraccionespendientes(ipservidor,con):
	select = selectbd.selectinteraccionpendiente(con)
	interacciones = select.fetchall()
	for interaccion in interacciones:
		filtrointeraccion(ipservidor,con,interaccion)