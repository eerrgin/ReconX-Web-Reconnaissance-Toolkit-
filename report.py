import json
import os
from datetime import datetime
from colorama import Fore, Style


def save(data, filename):
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    data["_meta"] = {
        "tool": "ReconX",
        "generated_at": datetime.utcnow().isoformat() + "Z"
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"{Fore.GREEN}[+] Rapor kaydedildi: {filename}{Style.RESET_ALL}")
