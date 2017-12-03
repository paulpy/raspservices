#!/usr/bin/env python
#comandogpio
import RPi.GPIO as GPIO
import time
import lograspadmin

def encender():
    lograspadmin.escribirlog("Encender equipo timepo 2 Segundos")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwaings(False)
    GPIO.setup(17,GPIO.HIGH)
    time.sleep(2)
    GPIO.setup(17,GPIO.LOW)

def apagar():
    lograspadmin.escribirlog("Apagar equipo timepo 5 Segundos")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwaings(False)
    GPIO.setup(17,GPIO.HIGH)
    time.sleep(5)
    GPIO.setup(17,GPIO.LOW)