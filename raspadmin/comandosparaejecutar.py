#!usr/bin/env python
#comandospararaspberrys
# -*- coding: utf-8 -*-

import subprocess
import os
import logging as log

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def apagarrasp():
    log.info('*****Comando apagar Raspberry*****')
    subprocess.call("shutdown")

def reiniciarrasp():
    log.info('*****Reiniciar Raspberry******')
    subprocess.call("reboot")

def cambiarfechahora(comando):
    log.info('*****Cambiar Fecha hora******')
    subprocess.call(comando)

def ejecutarcomandosgenerico(comando):
    log.info('*****Ejecutar comando generico*****')
    os.system(comando)
