import subprocess
import platform
import socket
def ping_host(ip):
    is_windows = platform.system().lower() == "windows"

    if is_windows:
        count_param = "-n"  # windows
    else:
        count_param = "-c"  # linux/mac

    command = ["ping", count_param, "1", ip]
    result = subprocess.call(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result == 0
    
def check_port(ip,port,timeout=2):
    try:
        with socket.create_connection((ip,port), timeout=timeout):
            return True
    except:
        return False