import subprocess
import known_host

known_hosts_full=subprocess.check_output(['cat','/Users/grahamskeats/.ssh/known_hosts'])
entry=[]
curr_string=''
for char in str(known_hosts_full):
    if char is '\n':
        continue
    if char is ' ':
        entry.append(curr_string)
        curr_string=''
    elif char is '=':
        entry.append(curr_string+'=')
        print(entry)
        entry=[]
        curr_string=''
    else:
        curr_string = curr_string + char

