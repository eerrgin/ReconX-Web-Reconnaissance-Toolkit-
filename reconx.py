#!/usr/bin/env python3
"""
ReconX - Web Reconnaissance Toolkit
For AUTHORIZED testing only. Use responsibly.
"""
import argparse
import sys
from colorama import init, Fore, Style
from modules import port_scanner, header_analyzer, ssl_checker, dns_lookup, report

init(autoreset=True)

BANNER = f"""{Fore.CYAN}
  ____                     __  __
 |  _ \\ ___  ___ ___  _ __  \\ \\/ /
 | |_) / _ \\/ __/ _ \\| '_ \\  \\  /
 |  _ <  __/ (_| (_) | | | | /  \\
 |_| \\_\\___|\\___\\___/|_| |_|/_/\\_\\
        Web Reconnaissance Toolkit v1.0
{Style.RESET_ALL}"""


def main():
    print(BANNER)
    parser = argparse.ArgumentParser(
        description="ReconX - Web reconnaissance toolkit (authorized use only)")
    parser.add_argument("-t", "--target", required=True, help="Hedef domain veya IP")
    parser.add_argument("--ports", default="1-1024", help="Port aralığı (örn: 1-1000)")
    parser.add_argument("--headers", action="store_true", help="HTTP header analizi")
    parser.add_argument("--ssl", action="store_true", help="SSL sertifika kontrolü")
    parser.add_argument("--dns", action="store_true", help="DNS kayıtları")
    parser.add_argument("--all", action="store_true", help="Hepsini çalıştır")
    parser.add_argument("-o", "--output", help="Rapor dosyası (JSON)")

    args = parser.parse_args()
    target = args.target.replace("https://", "").replace("http://", "").split("/")[0]
    results = {"target": target}

    print(f"{Fore.MAGENTA}[!] UYARI: Bu aracı yalnızca izinli sistemlerde kullan.{Style.RESET_ALL}\n")

    run_all = args.all

    if args.dns or run_all:
        results["dns"] = dns_lookup.run(target)
        print()

    if args.headers or run_all:
        results["headers"] = header_analyzer.run(target)
        print()

    if args.ssl or run_all:
        results["ssl"] = ssl_checker.run(target)
        print()

    if args.ports or run_all:
        results["ports"] = port_scanner.run(target, args.ports)

    if args.output:
        report.save(results, args.output)

    print(f"\n{Fore.CYAN}[✓] Tarama tamamlandı.{Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Kullanıcı tarafından durduruldu.{Style.RESET_ALL}")
        sys.exit(0)
