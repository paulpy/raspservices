"""
import logging as log
import ConfigParser
import os

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = 'loginiciosistema.log'
LEVEL_F = log.INFO
CONFIG_FILE_DIR = os.getcwd()
CONFIG_FILE_NAME = '/config.ini'

log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

user_input = raw_input('Ingrese palabra para el log: ')

log.info('Prueba de log')
log.info("Prueba de log")
log.info('Palabra: %r', user_input)

config = ConfigParser.ConfigParser()
config = ConfigParser(CONFIG_FILE_DIR + Con)
DEFAULT_PORT = config.get('main','default_app_port')


"""
import datetime
import time

t1 = datetime.datetime.now()
time.sleep(2)
t2 = datetime.datetime.now()

resultadotiempo = t2 - t1

secundos = int(resultadotiempo.total_seconds())

print secundos
