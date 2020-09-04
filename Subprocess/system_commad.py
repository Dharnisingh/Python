# Execute system command using subprocess module
# process_obj = subprocess.run('cmd', shell=True, capture_output= True, text= True, check= True)
# shell = True ==> Allows to pass command as single string insteal as list of arguments(['ls', '-l'])
# text = True ==> get output from process_obj as string process_obj.stdout
# capture_output ==> Allows to cature output of command into variable
# stdout = file_ob ==> top redirect command output to file
# input = sub_obj.stdout ==> Taking output of once command as input to other
import subprocess
sub_obj = subprocess.run('ls -l dirs', shell=True, capture_output=True, text=True)

print(sub_obj.stdout)
print(sub_obj.args)
print(sub_obj.returncode)
print(sub_obj.stderr)
print(dir(sub_obj))

# Redirect output to a file
with open('out.txt','w') as f:
    sub_obj = subprocess.run('ps -a', shell=True, stdout=f, text=True)
