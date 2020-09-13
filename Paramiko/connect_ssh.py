# Make ssh connection and execute command on remote machine using Paramiki
from paramiko import SSHClient
import paramiko

client = SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("localhost", username="dharni", password="system")

stdin, stdout, stderr = client.exec_command("echo 'Hello\n'")

stdin.write("ls -l")

print("STDOUT:", stdout.read().decode("utf8"))
stdin, stdout, stderr = client.exec_command("ls -l")
#print("STDOUT:", stdout.read().decode("utf8"))
print("STDERR:", stderr.read().decode("utf8"))

st = stdout.read().decode("utf8").split('\n')
for ch in st:
    print("1: ", ch)
# Close the client itself
client.close()
