import ipaddress
class host:

    def __init__(self, name, key_type_string, key_string, descrip=None):
        self.names = name
        if ',' in self.names:
            name_split = name.split(',')
            self.domain_name=name_split[0]
            self.ip_addr=ipaddress.ip_address(name_split[1])
        else:
            self.ip_addr=ipaddress.ip_address(name)
        self.key=key_string
        self.key_type=key_type_string
        self.description=descrip


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



    def find_entry(self,ip=None,domainName=None):
        if ip is None and domainName is None:
            ip=input("ip address is: ")
            return
        for entry in self.host_list:
            if entry.domain_name is domainName or entry.ip_addr is ip:
                return entry
        print("Entry not found, check that it does exist and you have entered its identifyng information correctly")
        return None

    def add_description(self,ip=None,domainName=None):
        entry=self.find_entry(ip,domainName)
        entry.description="#"+input("Type the description for this entry here: ")

        return

    def write_known_hosts(self):
        pipe=open("/Users/grahamskeats/.ssh/test","w")
        for entry in self.host_list:
            pipe.write(entry.names+" ")
            pipe.write(entry.key_type+" ")
            pipe.write(entry.key)
            if entry.description is not None:
                pipe.write("\n")
                pipe.write(entry.description)
            pipe.write("\n")
        pipe.close()
        return