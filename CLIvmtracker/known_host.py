import ipaddress
class known_host:

    def __init__(self,ip, key_string, key_type_string, descrip, first_name=None, ):
        domain_name=first_name
        ip_addr=ipaddress.ip_address(ip)
        key=key_string
        key_type=key_type_string
        description=descrip
