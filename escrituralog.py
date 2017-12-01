#!usr/bin/env python
#escrituradellog

import datetime

def escribirlog(escritura):
	momento = datetime.datetime.now()
	f = open("loginicio.txt", "a")
	f.write("\n"+str(momento)+" "+str(escritura))
	f.close()