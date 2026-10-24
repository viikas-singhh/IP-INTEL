# IP-INTEL 🌐🔍

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.1.0-purple.svg)](https://github.com/viikas-singhh/IP-INTEL)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-green.svg)]()

> **Public IP Intelligence & Reconnaissance Tool**  
> An interactive command-line reconnaissance engine designed for security analysts, incident responders, network administrators, and OSINT researchers to profile IP addresses instantly.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [UI & Output Preview](#-ui--output-preview)
- [Architecture & Data Sources](#-architecture--data-sources)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Interactive Commands](#-interactive-commands)
- [How to Push to GitHub](#-how-to-push-to-github)
- [Project Structure](#-project-structure)
- [Disclaimer & Ethics](#-disclaimer--ethics)
- [Author & License](#-author--license)

---

## 🚀 Overview

**IP-INTEL** is a fast, terminal-based Open Source Intelligence (OSINT) tool that aggregates deep network metadata, geographic positioning, security threat indicators, and ownership records for any target IPv4 or IPv6 address. 

With zero API key configuration needed, it turns raw IP addresses into actionable intelligence cards within milliseconds through an interactive, color-coded terminal dashboard.

---

## ✨ Key Features

| Category | Capabilities |
| :--- | :--- |
| **🎯 Target Scope Analysis** | Strict IPv4/IPv6 validation, detects whether IP is **Public**, **Private**, **Loopback**, **Link-Local**, **Multicast**, or **Reserved** (prevents unnecessary public API calls for local ranges). |
| **📍 Geolocation Intelligence** | Detailed physical location data: **Country**, **Country Code**, **Region/State**, **City**, **Postal Code**, **GPS Coordinates** (Latitude/Longitude), and **Local Timezone**. |
| **🌐 Network & ASN Profiling** | Autonomous System Number (**ASN**), Internet Service Provider (**ISP**), registered **Organization**, and parent **Domain**. |
| **🛡️ Threat & Anonymity Flags** | Identifies potential anonymity layers and threat vectors: **VPN**, **Proxy**, **Tor Exit Nodes**, and **Cloud/Hosting/Datacenter** infrastructure. |
| **📋 RDAP & Network Ownership** | Queries modern Registration Data Access Protocol (RDAP) for registry handles, network range allocations (`startAddress` to `endAddress`), registry names, and governing RIRs (ARIN, RIPE, APNIC, LACNIC, AFRINIC). |
| **🚨 Abuse Contact Extraction** | Automatically parses complex RDAP `vCard` directory structures to retrieve verified security contacts: **Abuse Desk Name**, **Abuse Email**, and **Telephone Number**. |
| **🔍 Reverse DNS / PTR** | Resolves hostnames and PTR records via reverse DNS queries. |
| **💻 Interactive Terminal Interface** | Features an interactive shell prompt (`ENTER-IP ❯`), colored ASCII art header, ANSI double-line framed output boxes, and automatic word-wrapping for long strings. |

---

## 🖥️ UI & Output Preview

```text
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║   ██╗██████╗       ██╗███╗   ██╗████████╗███████╗██╗      ║
║   ██║██╔══██╗      ██║████╗  ██║╚══██╔══╝██╔════╝██║      ║
║   ██║██████╔╝█████╗██║██╔██╗ ██║   ██║   █████╗  ██║      ║
║   ██║██╔═══╝ ╚════╝██║██║╚██╗██║   ██║   ██╔══╝  ██║      ║
║   ██║██║           ██║██║ ╚████║   ██║   ███████╗██║      ║
║   ╚═╝╚═╝           ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝      ║
║                                                            ║
║                     I P - I N T E L                        ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
────────────────────────────────────────────────────────────
 Version : 1.1.0
 Author  : Vikas Singh
 Purpose : Public IP intelligence & reconnaissance
────────────────────────────────────────────────────────────

Type 'help' for available commands.

ENTER-IP ❯ 8.8.8.8

[+] Target accepted: 8.8.8.8

[*] Running IP reconnaissance...
    ├─ Target analysis

╭────────────────────────────────────────────────────────────────────────╮
│ TARGET                                                                 │
├────────────────────────────────────────────────────────────────────────┤
│ IP Address         : 8.8.8.8                                           │
│ IP Version         : IPv4                                              │
│ Type               : PUBLIC                                            │
│ Global             : YES                                               │
│ Loopback           : NO                                                │
╰────────────────────────────────────────────────────────────────────────╯

[*] Querying IP intelligence source...

╭────────────────────────────────────────────────────────────────────────╮
│ GEOLOCATION                                                            │
├────────────────────────────────────────────────────────────────────────┤
│ Country            : United States                                     │
│ Country Code       : US                                                │
│ Region             : California                                        │
│ City               : Mountain View                                     │
│ Postal Code        : 94043                                             │
│ Coordinates        : 37.4223, -122.0848                                │
│ Timezone           : America/Los_Angeles                               │
╰────────────────────────────────────────────────────────────────────────╯

╭────────────────────────────────────────────────────────────────────────╮
│ NETWORK                                                                │
├────────────────────────────────────────────────────────────────────────┤
│ ASN                : AS15169                                           │
│ Organization       : Google LLC                                        │
│ ISP                : Google LLC                                        │
│ Domain             : google.com                                        │
╰────────────────────────────────────────────────────────────────────────╯

[*] Querying RDAP ownership data...

╭────────────────────────────────────────────────────────────────────────╮
│ OWNERSHIP                                                              │
├────────────────────────────────────────────────────────────────────────┤
│ Handle             : NET-8-8-8-0-1                                     │
│ Network Name       : GOGL                                              │
│ Start Address      : 8.8.8.0                                           │
│ End Address        : 8.8.8.255                                         │
│ Country            : US                                                │
│ Registry           : whois.arin.net                                    │
╰────────────────────────────────────────────────────────────────────────╯

╭────────────────────────────────────────────────────────────────────────╮
│ SECURITY / REPUTATION                                                  │
├────────────────────────────────────────────────────────────────────────┤
│ VPN                : NO                                                │
│ Proxy              : NO                                                │
│ Tor                : NO                                                │
│ Hosting            : NO                                                │
╰────────────────────────────────────────────────────────────────────────╯

╭────────────────────────────────────────────────────────────────────────╮
│ DNS                                                                    │
├────────────────────────────────────────────────────────────────────────┤
│ Reverse DNS        : dns.google                                        │
│ PTR                : dns.google                                        │
╰────────────────────────────────────────────────────────────────────────╯

╭────────────────────────────────────────────────────────────────────────╮
│ ABUSE CONTACT                                                          │
├────────────────────────────────────────────────────────────────────────┤
│ Name               : Google LLC                                        │
│ Email              : network-abuse@google.com                          │
│ Phone              : +1-650-253-0000                                   │
╰────────────────────────────────────────────────────────────────────────╯

[+] Reconnaissance complete.
────────────────────────────────────────────────────────────
```

---

## 📡 Architecture & Data Sources

IP-INTEL queries trusted, publicly available intelligence feeds without requiring private API tokens:

1. **IP Intelligence API (`ipwho.is`)**: Provides real-time geolocation, ASN data, ISP mapping, and proxy/VPN/Tor classification.
2. **RDAP API (`rdap.org`)**: Queries authoritative regional Internet registry records (ARIN, RIPE NCC, APNIC, LACNIC, AFRINIC) to extract allocation blocks and abuse points of contact.
3. **Local Socket Engine (`socket`)**: Performs reverse DNS queries locally to detect PTR records.
4. **Standard Library `ipaddress`**: Performs offline mathematical IP validation and classification before any external HTTP traffic is initiated.

---

## 📦 Requirements

- **Python**: `3.8` or newer
- **Operating System**: Linux, macOS, or Windows
- **Dependencies**: Listed in `requirements.txt`
  - `requests >= 2.31.0`

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/viikas-singhh/IP-INTEL.git
cd IP-INTEL
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📖 How to Use

Launch the tool by running:

```bash
python ip-intel.py
```

Once loaded, you will be greeted by the interactive console:
```text
ENTER-IP ❯ 
```

Type any IPv4 or IPv6 address and press `Enter` to run full reconnaissance.

---

## ⌨️ Interactive Commands

Inside the IP-INTEL interactive shell, the following commands are available:

| Command | Description |
| :--- | :--- |
| `<IP Address>` | Analyze any target public IPv4 or IPv6 address (e.g., `8.8.8.8` or `2606:4700:4700::1111`) |
| `help` or `?` | Displays built-in help manual with command descriptions and examples |
| `clear` | Clears the terminal screen and reprints the banner |
| `version` | Shows the current IP-INTEL application version and author metadata |
| `exit`, `quit`, `q` | Safely terminates and exits the application (or press `Ctrl+C`) |

---

## 🐙 How to Push to GitHub

To push this project to your repository at [https://github.com/viikas-singhh/IP-INTEL.git](https://github.com/viikas-singhh/IP-INTEL.git), follow these steps in your terminal:

```bash
# 1. Initialize git in the project directory
git init

# 2. Stage all project files (code, readme, requirements, gitignore)
git add .

# 3. Create your initial commit
git commit -m "Initial commit: IP-INTEL v1.1.0 release"

# 4. Set the default branch to main
git branch -M main

# 5. Add your GitHub repository as the remote origin
git remote add origin https://github.com/viikas-singhh/IP-INTEL.git

# 6. Push your commits to GitHub
git push -u origin main
```

> **Note:** If your remote repository already has an existing `README` or commit, run `git pull origin main --rebase` before `git push -u origin main`.

---

## 📂 Project Structure

```text
IP-INTEL/
├── .gitignore         # Ignores bytecode, venv, and cache files
├── ip-intel.py        # Core intelligence and CLI application engine
├── requirements.txt   # Project dependencies (requests)
└── README.md          # Comprehensive documentation and usage manual
```

---

## ⚖️ Disclaimer & Ethics

This tool is designed for educational purposes, defensive network analysis, incident triage, and authorized threat intelligence research. Ensure compliance with all applicable local, national, and international laws when gathering intelligence.

---

## 👤 Author & License

- **Author**: Vikas Singh
- **Repository**: [viikas-singhh/IP-INTEL](https://github.com/viikas-singhh/IP-INTEL.git)
- **License**: Distributed under the [MIT License](LICENSE).
