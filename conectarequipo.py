import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('192.168.1.56',port=22,username='root',password='DEStruccion93')
stdin,stdout,stderr = ssh.exec_command('reboot')
output = stdout.readlines()
print "\n".join(output)