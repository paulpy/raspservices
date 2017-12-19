#!/usr/bin/env python
#diferenciatiempo
# -*- coding: UTF-8 -*-

import logging as log
import datetime

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def diferenciadehora(fecha1,fecha2):
    log.info('*****Metodo de diferencia en hora******')
    data1 = fecha1
    data2 = fecha2
    resultadotiempo = data2 - data1
    segundos = int(resultadotiempo.total_seconds())
    return segundos
    log.info('******fin del metodo*****')
