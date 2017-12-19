#!/usr/bin/env python
#comandogpio
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import logging as log

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

def encender():
    log.info('*****Ingreso al metodo GPIO encender*****')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(17, GPIO.LOW)
    log.info('*******Fin del metodo******')

def apagar():
    log.info('*****Ingreso al metodo GPIO encender*****')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(17, GPIO.LOW)
    log.info('*****Fin del metodo*****')
