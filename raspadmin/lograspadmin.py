#!usr/bin/env python
#lograspadmin

import datetime

def escribirlog(escritura):
	momento = datetime.datetime.now()
	f = open("lograspadmin.txt", "a")
	f.write("\n"+str(momento)+" "+str(escritura))
	f.close()