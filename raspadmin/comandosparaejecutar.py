#!usr/bin/env python
#comandospararaspberrys

import subprocess
import os

def apagarrasp():
	subprocess.call("shutdown")

def reiniciarrasp():
	subprocess.call("reboot")

def cambiarfechahora(comando):
	print "llego hasta aca"
	subprocess.call(comando)

def ejecutarcomandosgenerico(comando):
	os.system(comando)