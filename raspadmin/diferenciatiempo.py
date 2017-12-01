#!/usr/bin/env python
#diferenciatiempo

import datetime

def diferenciadehroa(date1,date2):
    data1 = datetime.datetime.now()
    data2 = datetime.datetime.now()
    diff = data2 - data1
    seconds = diff.seconds
    seconds = seconds % 60
    return seconds