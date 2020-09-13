#!/usr/bin/python3
import pexpect

child = pexpect.spawn('ssh root@192.168.0.114')
child.expect('.* password: ', timeout=120)
child.sendline('system')

child.expect('.*#')
print (child.after.decode())

child.sendline('uname -a')
child.expect('.*# ')
print (child.after.decode())
#child.run('ls -la')
child.sendline('ls -la')
child.expect('.*# ')

str = child.after.decode()
print("=====Output of LS command====")
for i in list(str.split('\n')):
    print(i)

print("=====End of Output of LS command====")
count =0
while  child.isalive():
    print(count)
    if count == 5:
        # Close the session
        child.close()
    count +=1

if child.isalive():
    print('Child did not exit gracefully.')
else:
    print('Child exited gracefully.')
