import dns.resolver
from colorama import Fore, Style

RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]


def run(domain):
    print(f"{Fore.CYAN}[*] DNS kayıtları: {domain}{Style.RESET_ALL}")
    results = {}

    for rtype in RECORD_TYPES:
        try:
            answers = dns.resolver.resolve(domain, rtype, lifetime=5)
            values = [str(r) for r in answers]
            results[rtype] = values
            print(f"{Fore.GREEN}[+] {rtype:6} -> {', '.join(values)}{Style.RESET_ALL}")
        except Exception:
            pass

    return results
