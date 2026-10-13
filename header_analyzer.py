import requests
from colorama import Fore, Style

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


def run(target):
    url = target if target.startswith("http") else f"https://{target}"
    print(f"{Fore.CYAN}[*] Header analizi: {url}{Style.RESET_ALL}")

    try:
        r = requests.get(url, timeout=10, allow_redirects=True,
                         headers={"User-Agent": "ReconX/1.0"})
    except Exception as e:
        print(f"{Fore.RED}[!] Bağlantı hatası: {e}{Style.RESET_ALL}")
        return {}

    results = {"url": url, "status": r.status_code,
               "present": [], "missing": []}

    print(f"{Fore.WHITE}[i] Status: {r.status_code}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[i] Server: {r.headers.get('Server', 'N/A')}{Style.RESET_ALL}\n")

    for h in SECURITY_HEADERS:
        if h in r.headers:
            print(f"{Fore.GREEN}[+] {h}: {r.headers[h]}{Style.RESET_ALL}")
            results["present"].append(h)
        else:
            print(f"{Fore.RED}[-] {h} EKSİK{Style.RESET_ALL}")
            results["missing"].append(h)

    score = len(results["present"]) * 100 // len(SECURITY_HEADERS)
    color = Fore.GREEN if score >= 70 else Fore.YELLOW if score >= 40 else Fore.RED
    print(f"\n{color}[=] Güvenlik Skoru: {score}/100{Style.RESET_ALL}")
    results["score"] = score
    return results
