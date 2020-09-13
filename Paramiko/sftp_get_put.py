# Implementation of sftp to get and put files on remote machine
import paramiko
from paramiko import SSHClient

ssh = SSHClient()
# Add entry of remote host to known host list at local 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establish ssh conection
ssh.connect('localhost', username='dharni', password='system')
print("Connection Established: ")

# Open ftp client using ssh connection object
ftp_client = ssh.open_sftp()
# Fethc file from 1st arg to current directory
ftp_client.get("/home/dharni/a.out","a.out")
# Send file AAAA from current folder to destination folder
ftp_client.put("AAAA", "/home/dharni/AAAA")
# Done with trancfer 
# Close the ftp session
ftp_client.close()
# Close ssh connection
ssh.close()
