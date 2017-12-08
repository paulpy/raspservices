#!usr/bin/env python
#registrarhistorico

import datetime
import logging as log
import escrituralog

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = 'loginiciosistema.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def historicoraspberry(causa, estado, con):
	cursor = con.cursor()
	log.debug('Ingreso al metodo historicoraspberry')
	log.info('Insercion en HistoricoRaspberry')
	fechahora = datetime.datetime.now()
	log.debug('Insercion en la Base de Datos')
	cursor.execute("INSERT INTO raspapp_historico_estado_raspberry (fecha_hora_equipo_raspberry, causa_raspberry_fk_id, estado_raspberry_fk_id, raspberry_asignado_fk_id) VALUES (\'"+str(fechahora)+"\' ,"+str(causa)+","+str(estado)+",1)")
	con.commit()
	log.debug('Guardado en la Base de datos')
	log.info('Finaliando Metodo')
	log.info('-------------------------------------')

def historicoequipo(causa, estado, con):
	cursor = con.cursor()
	log.debug('Ingreso al metodo historicoraspberry')
	log.info('Insercion en HistoricoRaspberry')
	fechahora = datetime.datetime.now()
	log.debug('Insercion en la Base de Datos')
	cursor.execute("INSERT INTO raspapp_historico_estado_equipo (fecha_hora_equipo_estado, causa_equipo_fk_id, estado_equipo_fk_id, equipo_asignado_fk_id) VALUES (\'"+str(fechahora)+"\' ,"+str(causa)+","+str(estado)+",1)")
	con.commit()
	log.debug('Guardado en la Base de datos')
	log.info('Finaliando Metodo')
	log.info('-------------------------------------')
