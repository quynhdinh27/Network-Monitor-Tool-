import ipaddress
import socket

def resolve_host(host):
    try:
        ipaddress.ip_address(host)
        return host
    except ValueError:
        try:
            return socket.gethostbyname(host)
        except socket.gaierror:
            return None