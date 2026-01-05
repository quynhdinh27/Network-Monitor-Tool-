from host import resolve_host
from network import ping_host, check_port
from logger import write_log
 

def check_host_status(host, ports=None):
    """Check host reachability and common ports.

    Returns a dict with keys: host, ip, ping, open_ports, status, log
    """
    ports_to_check = ports or [22, 80, 443]
    log_lines = [f"Checking host: {host}"]

    ip = resolve_host(host)
    if ip is None:
        status = "CANNOT RESOLVE HOST"
        log_lines.append(status)
        log_text = "\n".join(log_lines)
        write_log(log_text)
        print(log_text)
        return {
            "host": host,
            "ip": None,
            "ping": False,
            "open_ports": [],
            "status": status,
            "log": log_text,
        }

    log_lines.append(f"Resolved IP: {ip}")
    ping_ok = ping_host(ip)
    log_lines.append("Ping: OK" if ping_ok else "Ping: FAIL")

    open_ports = []
    for port in ports_to_check:
        if check_port(ip, port):
            log_lines.append(f"Port {port}: OPEN")
            open_ports.append(port)
        else:
            log_lines.append(f"Port {port}: CLOSED")

    if ping_ok and open_ports:
        status = "ONLINE - SERVICE ACTIVE"
    elif ping_ok:
        status = "ONLINE - NO SERVICE"
    else:
        status = "UNREACHABLE"

    log_lines.append(f"Overall status: {status}")
    log_text = "\n".join(log_lines)

    write_log(log_text)

    # Print output
    for line in log_lines:
        print(line)

    return {
        "host": host,
        "ip": ip,
        "ping": ping_ok,
        "open_ports": open_ports,
        "status": status,
        "log": log_text,
    }
