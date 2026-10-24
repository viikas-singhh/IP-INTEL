# IP-INTEL

A simple command-line tool to gather intelligence and reconnaissance data on public IPv4 and IPv6 addresses. It queries public APIs to retrieve geolocation, network/ISP details, RDAP ownership, security flags, and abuse contact information without requiring any API keys.

---

## Features

- **Target Analysis**: Validates IPv4/IPv6 and checks if the address is Public, Private, Loopback, or Reserved.
- **Geolocation**: Country, region, city, postal code, geographic coordinates, and timezone.
- **Network & ASN**: Autonomous System Number (ASN), ISP, organization, and domain.
- **Ownership (RDAP)**: Network name, handle, allocated IP address range, and regional registry.
- **Security & Anonymity**: Detects if the IP is flagged as a VPN, Proxy, Tor exit node, or Hosting/Datacenter.
- **Reverse DNS**: Resolves hostnames and PTR records.
- **Abuse Contacts**: Extracts security and abuse contact details (name, email, phone) from RDAP records.
- **Interactive Shell**: Clean terminal interface with built-in commands and color formatting.

---

## Requirements

- Python 3.8 or higher
- `requests` library

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/viikas-singhh/IP-INTEL.git
   cd IP-INTEL
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script:

```bash
python ip-intel.py
```
*(On Windows, you can also use `py ip-intel.py`)*

Once the tool opens, enter any public IP address at the prompt:

```text
ENTER-IP ❯ 8.8.8.8
```

### Available Commands

| Command | Description |
| :--- | :--- |
| `<IP>` | Analyze an IP address (e.g. `8.8.8.8` or `2001:4860:4860::8888`) |
| `help` | Show available commands and examples |
| `clear` | Clear the screen and reprint banner |
| `version` | Show version information |
| `exit` | Quit the tool (or use `quit` / `q`) |

---

## Example Output

```text
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
```

---

## Author

- **Vikas Singh**
- Repository: [https://github.com/viikas-singhh/IP-INTEL](https://github.com/viikas-singhh/IP-INTEL)
