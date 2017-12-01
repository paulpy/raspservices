#!/bin/bash

echo iniciando server puerto 8000
source /root/raspadmin/bin/activate
python /root/raspadmin/raspweb/manage.py runserver 0:8000
