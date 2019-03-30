import subprocess
import host



def get_hosts():
    known_hosts_full=subprocess.check_output(['cat','/Users/grahamskeats/.ssh/known_hosts'])
    entry=[]
    known_hosts_full=known_hosts_full.decode('utf-8')
    host_list=[]
    line_split=known_hosts_full.split('\n')
    iter_splits=iter(line_split)

    for line in iter_splits:
        if line is '':
            continue
        if checkforcomment(line):
            host_list[-1].description=line
            continue
        split_line=line.split()
        for split in split_line:
            entry.append(split)
            if '=' in split:
                new_host = host.host(entry[0], entry[1], entry[2])
                entry = []
                host_list.append(new_host)
    return host_list


def checkforcomment(line):
    if line[0] is '#':
        return True
    else:
        return False
