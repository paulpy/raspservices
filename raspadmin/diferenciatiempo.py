#!/usr/bin/env python
#diferenciatiempo

import datetime

def diferenciadehora(fecha1,fecha2):
    data1 = fecha1
    data2 = fecha2
    diferencia = data2 - data1
    segundos = diferencia.seconds
    segundos = segundos % 60
    return segundos