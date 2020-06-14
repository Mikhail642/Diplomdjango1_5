import paramiko

host = '95.189.97.10'
user = 'um'
secret = 'Pf,fqrfkmcrbqRhfqum1'
port = 22315

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname=host, username=user, password=secret, port=port)


stdin, stdout, stderr = client.exec_command('ls -l')

data = stdout.read() + stderr.read()
client.close()