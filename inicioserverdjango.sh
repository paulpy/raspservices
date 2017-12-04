#!/bin/bash

echo iniciando server puerto 8000
source /root/raspproyect/bin/activate
python /root/raspproyect/raspweb/manage.py runserver 0:8000
