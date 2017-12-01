#!/usr/bin/env python
#lecturaestado

import comandogpio
import registrarenbd
import selectbd
import diferenciatiempo

import datetime

def lecturaestadoequipo(con):
    historico = selectbd.selectultimohee(con)
    estadoactual = historico.fetchone()
    if estadoactual[3]=="2":
        comandogpio.encender()
        registrarenbd.historicoequipo("3","6",con)
    if estadoactual[3]=="6":
        diferencia=diferenciatiempo(estadoactual[1],datetime.datetime.now)
        if diferencia > 200:
            registrarenbd.historicoequipo("3","4",con)
        else:
            pass
