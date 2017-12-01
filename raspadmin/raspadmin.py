#!usr/bin/env python
#raspadmin

import sqlite3
import lograspadmin
import registrarenbd
import pingserver
import consumidorserviciosweb
import lecturaestados
import cumplimientoaccion

con = sqlite3.connect("/root/raspadmin/raspweb/db.sqlite3")
ipservidor = "192.168.43.116"
ipequipo = "192.168.0.51"
lograspadmin.escribirlog("Inicio del RaspAdmin")
registrarenbd.historicoraspberry("6","5",con)
con.close()
def raspprocess():
	con = sqlite3.connect("/root/raspadmin/raspweb/db.sqlite3")
	lecturaestados.equipoconectado(con,ipequipo)
	if pingserver.isAlive(ipservidor):
		lograspadmin.escribirlog("Ping al Servidor")
		lograspadmin.escribirlog("Envio del historicoraspberry")
		consumidorserviciosweb.enviarlograsp(ipservidor,con)
		lograspadmin.escribirlog("Envio del historicoequipo")
		consumidorserviciosweb.enviarlogequi(ipservidor,con)
		lograspadmin.escribirlog("Trayendo Interacciones del Servidor")
		consumidorserviciosweb.interaccionws(ipservidor,con)
		lograspadmin.escribirlog("Cumpliendo Interacciones del Servidor")
		cumplimientoaccion.realizarinteraccionespendientes(ipservidor,con)
	else:
		lograspadmin.escribirlog("No existe conexion con el servidor")
	lecturaestados.lecturaestadoequipo(con)
	con.close()
	lograspadmin.escribirlog("Esperando 10 Segundos para reinicio")
	time.sleep(10)

while True:
	raspprocess()