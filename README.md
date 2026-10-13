# 🔍 ReconX — Web Reconnaissance Toolkit

> Lightweight web security reconnaissance tool for **authorized testing only**.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized penetration testing only**.
Do **NOT** use it against systems you do not own or do not have explicit written permission to test.
The author is not responsible for any misuse.

## ✨ Features

- 🔌 TCP Port Scanner (multi-threaded)
- 🛡️ HTTP Security Header Analyzer
- 🔐 SSL/TLS Certificate Inspector
- 🌐 DNS Lookup (A, MX, NS, TXT)
- 📄 JSON / TXT Report Generator
- 🎨 Clean CLI with colored output

## 🚀 Installation

```bash
git clone https://github.com/<kullanici-adin>/ReconX.git
cd ReconX
pip install -r requirements.txt
```

## 🧠 Usage

```bash
# Port taraması
python reconx.py -t example.com --ports 1-1000

# Header analizi
python reconx.py -t example.com --headers

# SSL sertifika kontrolü
python reconx.py -t example.com --ssl

# DNS kayıtları
python reconx.py -t example.com --dns

# Hepsini çalıştır
python reconx.py -t example.com --all

# Rapor kaydet
python reconx.py -t example.com --all -o report.json
```

## 📌 Legal

Only use on systems you own or have permission to test.
