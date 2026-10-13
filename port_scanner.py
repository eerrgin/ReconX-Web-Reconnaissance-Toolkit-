import socket
import concurrent.futures
from colorama import Fore, Style

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 6379: "Redis",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB"
}


def scan_port(host, port, timeout=1.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                service = COMMON_PORTS.get(port, "unknown")
                return port, service
    except Exception:
        pass
    return None


def parse_ports(port_str):
    ports = []
    for part in port_str.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            ports.extend(range(start, end + 1))
        else:
            ports.append(int(part))
    return ports


def run(host, port_range="1-1024", threads=100, timeout=1.5):
    print(f"{Fore.CYAN}[*] Port taraması başlatılıyor: {host}{Style.RESET_ALL}")
    ports = parse_ports(port_range)
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, host, p, timeout): p for p in ports}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                port, service = res
                print(f"{Fore.GREEN}[+] {port}/tcp açık  ->  {service}{Style.RESET_ALL}")
                open_ports.append({"port": port, "service": service})

    if not open_ports:
        print(f"{Fore.YELLOW}[-] Açık port bulunamadı.{Style.RESET_ALL}")
    return open_ports
