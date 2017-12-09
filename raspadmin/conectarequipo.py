#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Module to handle SSH Connections - Paramiko
"""
import paramiko
import pingserver
import lograspadmin
import logging as log

FORMAT_LOG = '%(asctime)s : %(levelname)s : %(message)s'
FILE_NAME = '/opt/raspservices/raspadmin/lograspadmin.log'
LEVEL_F = log.INFO
log.basicConfig(level=LEVEL_F, format=FORMAT_LOG, filename=FILE_NAME)

C_SERVER = '192.168.12.28'
C_PORT = 22
C_USER = 'root'
C_PASS = 'DEStruccion93'

def cumplicomando(comando):
    """
    cumplicomando
    Connect throught SSH and get a shell prompt from a host
    Arguments: str: comando
    """
    log.info('*****Ingresando a Metodo cumplir comando en equipo asignado*****')
    if pingserver.isAlive(C_SERVER):
        log.info('*****Hay pign con el equipo intentado cumplir comando*****')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(C_SERVER, port=C_PORT, username=C_USER, password=C_PASS)
        stdin, stdout, stderr = ssh.exec_command(str(comando))
        output = stdout.readlines()
        log.info('Mensaje del comando cumplido'.join(output))
        log.info('-------------------------------------------')
    else:
        log.info('*****No existe conexion con el equipo orden no cumplida*****')
        pass
