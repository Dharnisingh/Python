# Connect using ssh key to EC2 instance
from paramiko import SSHClient
import paramiko
client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('ec2-18-221-93-115.us-east-2.compute.amazonaws.com',
            username='ec2-user',
            key_filename='ec2_key.pem')

stdin, stdout, stderr = client.exec_command("uptime;ls -l;touch mickymouse;ls -l;uptime")
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print(line)
client.close()


