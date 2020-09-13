# porgram to print stats of file
import os
import shutil
import time

def file_metadata(file_name):
    stat_info = os.stat(file_name)
    print('  Mode    :', oct(stat_info.st_mode))
    print('  Created :', time.ctime(stat_info.st_ctime))
    print('  Accessed:', time.ctime(stat_info.st_atime))
    print('  Modified:', time.ctime(stat_info.st_mtime))

os.mkdir('journaldev')
print('SOURCE FILE:')
file_metadata('file_stat_data.py')

shutil.copy2('file_stat_data.py', 'journaldev')

print('DESTINATION FILE:')
file_metadata('journaldev/file_stat_data.py')

# Remove directory journaldev recurcively
shutil.rmtree("journaldev")
