import subprocess
import host



def get_hosts():
    known_hosts_full=subprocess.check_output(['cat','/Users/grahamskeats/.ssh/known_hosts'])
    entry=[]
    known_hosts_full=known_hosts_full.decode('utf-8')
    host_list=[]
    line_split=known_hosts_full.split('\n')
    iter_splits=iter(line_split)
    completeentry = False

    for line in iter_splits:
        if line is '':
            continue
        comment=checkforcomment(line)
        if comment is not None or completeentry:
            new_host=host.host(entry[0], entry[1], entry[2], comment)
            entry=[]
            completeentry=False
            host_list.append(new_host)
            continue
        split_line=line.split()
        for split in split_line:
            entry.append(split)
            if '=' in split:
                completeentry=True

    return host_list


def checkforcomment(line):
    if line[0] is '#':
        return line
    else:
        return None


host_list=get_hosts()
host_mngr=host.host_manager()
host_mngr.load_host(host_list)
host_mngr.write_known_hosts()