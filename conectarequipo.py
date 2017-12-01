#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Module to handle SSH Connections - Paramiko
"""

import paramiko

C_SERVER = '192.168.1.56'
C_PORT = 22
C_USER = 'root'
C_PASS = 'DEStruccion93'

def cumplicomando(comando):
    """
    cumplicomando
    Connect throught SSH and get a shell prompt from a host
    Arguments: str: comando
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(C_SERVER, port=C_PORT, username=C_USER, password=C_PASS)
    stdin, stdout, stderr = ssh.exec_command(str(comando))
    output = stdout.readlines()
    print "\n".join(output)
