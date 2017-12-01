#!usr/bin/env python
#constructordeurls

def urlhistoricorasp(ipservidor,serie):
	urlhrasp = "http://"+ipservidor+":8080/sivig/rest/historicoraspberry/ultimosincronizado/"+str(serie)
	return urlhrasp

def urlsincrohistoricorasp(ipservidor):
	urlhrasp = "http://"+ipservidor+":8080/sivig/rest/historicoraspberry/sincronizarHistoricoEstado"
	return urlhrasp

def urlhistoricoequi(ipservidor,serie):
	urlhequi = "http://"+ipservidor+":8080/sivig/rest/historicoequipo/ultimosincronizado/"+str(serie)
	return urlhequi

def urlsincrohistoricoequi(ipservidor):
	urlhequi = "http://"+ipservidor+":8080/sivig/rest/historicoequipo/sincronizarHistoricoEstado"
	return urlhequi

def urlinteracciones(ipservidor):
	urlinteraccion = "http://"+ipservidor+":8080/sivig/rest/interaccion/interaccionpendiente"
	return urlinteraccion

def urlaccion(ipservidor):
	urlaccion = "http://"+ipservidor+":8080/sivig/rest/accioncausaestado/acciones"
	return urlaccion

def urlestado(ipservidor):
	urlaccion = "http://"+ipservidor+":8080/sivig/rest/accioncausaestado/estados"
	return urlaccion

def urlcausa(ipservidor):
	urlaccion = "http://"+ipservidor+":8080/sivig/rest/accioncausaestado/causas"
	return urlaccion

def urlactualizarinteraccion(ipservidor):
	urlainte = "http://"+ipservidor+":8080/sivig/rest/interaccion/interaccionactualizar"
	return urlainte