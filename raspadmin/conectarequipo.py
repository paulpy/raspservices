#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Module to handle SSH Connections - Paramiko
"""
import paramiko
import pingserver
import lograspadmin

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
    if pingserver.isAlive(C_SERVER):
        lograspadmin.escribirlog("Hay conexion con el equipo")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(C_SERVER, port=C_PORT, username=C_USER, password=C_PASS)
        stdin, stdout, stderr = ssh.exec_command(str(comando))
        output = stdout.readlines()
        print "\n".join(output)
    else:
        lograspadmin.escribirlog("No hay conexion con el equipo")
        pass
        