import subprocess
class host:

    def __init__(self, name, key_type_string, key_string, descrip=None):
        self.names = name
        if ',' in self.names:
            name_split = name.split(',')
            self.domain_name=name_split[0]
            self.ip_addr=name_split[1]
        else:
            self.domain_name=None
            self.ip_addr=name
        self.key=key_string
        self.key_type=key_type_string
        self.description=descrip
        self.username=None


class host_manager:

    def __init__(self):
        self.host_list=[]

    def load_host(self,*hosts):
        for item in hosts[0]:
            self.host_list.append(item)

    def delete_host(self,ip=None,domainName=None):
        entry=self.find_entry(ip,domainName)
        if entry is not None:
            self.host_list.remove(entry)
        return

    def find_entry(self,ip="",domainName=""):
        if ip is "" and domainName is "":
            ip=input("ip address is: ")
        for entry in self.host_list:
            if entry.domain_name==domainName or entry.ip_addr==ip:
                return entry
        print("Entry not found, check that it does exist and you have entered its identifyng information correctly")
        return None

    def add_description(self,ip="",domainName=""):
        entry=self.find_entry(ip,domainName)
        entry.description="#"+input("Type the description for this entry here: ")
        return

    def write_known_hosts(self):
        pipe=open("/Users/grahamskeats/.ssh/known_hosts","w")
        for entry in self.host_list:
            pipe.write(entry.names+" ")
            pipe.write(entry.key_type+" ")
            pipe.write(entry.key)
            if entry.description is not None:
                pipe.write("\n")
                pipe.write(entry.description)
            if entry.username is not None:
                pipe.write("   **Username:"+entry.username+"**")
            pipe.write("\n")
        pipe.close()
        return

    def print_available(self):
        for entry in self.host_list:
            if entry.description is not None:
                print(entry.names+"      "+entry.description)
            else:
                print(entry.names)

    def connect(self,host=None):
        host=self.find_entry(host)
        username=input("Username: ")
        host.username=username
        subprocess.call(['ssh',username+"@"+host.ip_addr])

    def readhostsfromfile(self):
        self.host_list=[]
        known_hosts_full = subprocess.check_output(['cat', '/Users/grahamskeats/.ssh/known_hosts'])
        entry = []
        known_hosts_full = known_hosts_full.decode('utf-8')
        host_list = []
        line_split = known_hosts_full.split('\n')
        iter_splits = iter(line_split)

        for line in iter_splits:
            if line is '':
                continue
            if self.checkforcomment(line):
                host_list[-1].description = line
                continue
            split_line = line.split()
            for split in split_line:
                entry.append(split)
                if '=' in split:
                    new_host = host(entry[0], entry[1], entry[2])
                    entry = []
                    host_list.append(new_host)
        self.load_host(host_list)
        return host_list

    def checkforcomment(self,line):
        if line[0] is '#':
            return True
        else:
            return False

    def createnewconnection(self,ip=None,username=None):
        if ip is None:
            ip=input("What is the ip address or domain name of the machine you would like to connect to: ")
        if username is None:
            username=input("What is your username: ")
        subprocess.call(['ssh',username+"@"+ip])
        self.readhostsfromfile()

    def checkduplicate(self,host):
        for entry in self.host_list:
            if host.ip_addr==entry.ip_addr:
                return True
        return False