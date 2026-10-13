import ssl
import socket
from datetime import datetime
from colorama import Fore, Style


def run(host, port=443):
    print(f"{Fore.CYAN}[*] SSL/TLS sertifika kontrolü: {host}:{port}{Style.RESET_ALL}")
    ctx = ssl.create_default_context()

    try:
        with socket.create_connection((host, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
    except Exception as e:
        print(f"{Fore.RED}[!] SSL hatası: {e}{Style.RESET_ALL}")
        return {}

    subject = dict(x[0] for x in cert.get("subject", []))
    issuer = dict(x[0] for x in cert.get("issuer", []))
    not_after = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
    days_left = (not_after - datetime.utcnow()).days

    print(f"{Fore.WHITE}[i] CN       : {subject.get('commonName')}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[i] Issuer   : {issuer.get('organizationName')}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[i] Bitiş    : {not_after}{Style.RESET_ALL}")

    if days_left < 0:
        print(f"{Fore.RED}[!] SERTİFİKA SÜRESİ DOLMUŞ!{Style.RESET_ALL}")
    elif days_left < 30:
        print(f"{Fore.YELLOW}[!] {days_left} gün kaldı — yakında yenilenmeli.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[+] Geçerli — {days_left} gün kaldı.{Style.RESET_ALL}")

    return {"subject": subject.get("commonName"),
            "issuer": issuer.get("organizationName"),
            "expires": str(not_after),
            "days_left": days_left}
